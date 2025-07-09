from sdks.novavision.src.helper.package import PackageHelper
from components.BlurExample.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, BlurExampleExecuterResponse, BlurExampleExecuter, OutputImage, BlurExampleExecuterOutputs


def build_response(context):
    outputImage = OutputImage(value=context.image)
    blurExampleOutputs = BlurExampleExecuterOutputs(outputImage=outputImage)  
    blurExampleExecuterResponse = BlurExampleExecuterResponse(outputs=blurExampleOutputs)
    blurExampleExecutor = BlurExampleExecuter(value=blurExampleExecuterResponse)
    executor = ConfigExecutor(value=blurExampleExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel