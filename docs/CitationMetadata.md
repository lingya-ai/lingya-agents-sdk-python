# CitationMetadata

CitationMetadata 的公开协议结构。 / Public contract for citation metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**reference_id** | **int** | 字段 referenceId / reference id field。 | 
**title** | **str** | 标题 / title。 | [optional] 
**description** | **str** | 可读说明 / human-readable description。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.citation_metadata import CitationMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CitationMetadata from a JSON string
citation_metadata_instance = CitationMetadata.from_json(json)
# print the JSON string representation of the object
print(CitationMetadata.to_json())

# convert the object into a dict
citation_metadata_dict = citation_metadata_instance.to_dict()
# create an instance of CitationMetadata from a dict
citation_metadata_from_dict = CitationMetadata.from_dict(citation_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


