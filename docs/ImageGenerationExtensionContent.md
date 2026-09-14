# ImageGenerationExtensionContent

ImageGenerationExtensionContent 的公开协议结构。 / Public contract for image generation extension content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **int** | 文件 ID / file ID。 | 

## Example

```python
from lingya_agents_sdk.models.image_generation_extension_content import ImageGenerationExtensionContent

# TODO update the JSON string below
json = "{}"
# create an instance of ImageGenerationExtensionContent from a JSON string
image_generation_extension_content_instance = ImageGenerationExtensionContent.from_json(json)
# print the JSON string representation of the object
print(ImageGenerationExtensionContent.to_json())

# convert the object into a dict
image_generation_extension_content_dict = image_generation_extension_content_instance.to_dict()
# create an instance of ImageGenerationExtensionContent from a dict
image_generation_extension_content_from_dict = ImageGenerationExtensionContent.from_dict(image_generation_extension_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


