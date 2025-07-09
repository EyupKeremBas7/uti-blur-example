"""
    It is one of the preprocessing components in which the image is rotated.
"""

import os
import cv2
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.BlurExample.src.utils.response import build_response
from components.BlurExample.src.models.PackageModel import PackageModel


class BlurExampleExecuter(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.rotation_degree = self.request.get_param("Degree")
        self.keep_side = self.request.get_param("KeepSide")
        self.image = self.request.get_param("inputImage")
        print(self.rotation_degree)
        print(self.keep_side)

    @staticmethod
    def bootstrap(config: dict) -> dict:
        sayac = 0
        return {"sayac" : sayac}
    
    def blur(self, image): 
        """
            Blurring the images
        """

        return cv2.blur(image,(10,10))
    
    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.blur(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response(context=self)
        self.bootstrap["sayac"] += 1
        print(self.bootstrap["sayac"])
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()