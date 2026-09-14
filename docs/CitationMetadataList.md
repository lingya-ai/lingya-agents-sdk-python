# CitationMetadataList

CitationMetadataList 的公开协议结构。 / Public contract for citation metadata list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[CitationMetadata]**](CitationMetadata.md) | 记录列表 / records。 | 

## Example

```python
from lingya_agents_sdk.models.citation_metadata_list import CitationMetadataList

# TODO update the JSON string below
json = "{}"
# create an instance of CitationMetadataList from a JSON string
citation_metadata_list_instance = CitationMetadataList.from_json(json)
# print the JSON string representation of the object
print(CitationMetadataList.to_json())

# convert the object into a dict
citation_metadata_list_dict = citation_metadata_list_instance.to_dict()
# create an instance of CitationMetadataList from a dict
citation_metadata_list_from_dict = CitationMetadataList.from_dict(citation_metadata_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


