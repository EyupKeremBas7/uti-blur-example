from pydantic import Field, validator
from typing import List, Optional, Union, Literal
from sdks.novavision.src.base.model import Package, Image, Inputs, Configs, Outputs, Response, Request, Output, Input, Config

class InputImage(Input):
    name: Literal["inputImage"] = "inputImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"


class OutputImage(Output):
    name: Literal["outputImage"] = "outputImage"
    value: Union[List[Image],Image]
    type: str = "object"


    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"

class Blur(Config):
    """
        Applies a blur to the image based on the given percentage.
    """
    name: Literal["Blur"] = "Blur"
    value: int = Field(ge=0, le=100.0,default=0)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["[0,100]"] = "[0,100]"

    class Config:
        title = "Blur"

class BlurExampleExecuterInputs(Inputs):
    inputImage: InputImage

class BlurExampleExecuterConfigs(Configs):
    blur: Blur

class BlurExampleExecuterRequest(Request):
    inputs: Optional[BlurExampleExecuterInputs]
    configs: BlurExampleExecuterConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }

class BlurExampleExecuterOutputs(Outputs):
    outputImage: OutputImage

class BlurExampleExecuterResponse(Response):
    outputs: BlurExampleExecuterOutputs


class BlurExampleExecuter(Config):
    name: Literal["BlurExampleExecuter"] = "BlurExampleExecuter"
    value: Union[BlurExampleExecuterRequest, BlurExampleExecuterResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Package"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }

class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[BlurExampleExecuter]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"
        json_schema_extra = {
            "target": "value"
        }

class PackageConfigs(Configs):
    executor: ConfigExecutor

class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["BlurExample"] = "BlurExample"
