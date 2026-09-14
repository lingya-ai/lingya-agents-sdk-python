# ImageGenerationExtensionToolExtension

ImageGenerationExtensionToolExtension 的公开协议结构。 / Public contract for image generation extension tool extension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | 扩展类别判别值 / extension category discriminator。 | 
**content** | [**ImageGenerationExtensionContent**](ImageGenerationExtensionContent.md) | 与类别对应的强类型内容 / strongly typed content for the category。 | 
**special_render** | **bool** | 是否使用独立视图渲染 / whether to use a dedicated view。 | 

## Example

```python
from lingya_agents_sdk.models.image_generation_extension_tool_extension import ImageGenerationExtensionToolExtension

# TODO update the JSON string below
json = "{}"
# create an instance of ImageGenerationExtensionToolExtension from a JSON string
image_generation_extension_tool_extension_instance = ImageGenerationExtensionToolExtension.from_json(json)
# print the JSON string representation of the object
print(ImageGenerationExtensionToolExtension.to_json())

# convert the object into a dict
image_generation_extension_tool_extension_dict = image_generation_extension_tool_extension_instance.to_dict()
# create an instance of ImageGenerationExtensionToolExtension from a dict
image_generation_extension_tool_extension_from_dict = ImageGenerationExtensionToolExtension.from_dict(image_generation_extension_tool_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


