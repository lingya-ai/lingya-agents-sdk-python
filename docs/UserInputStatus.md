# UserInputStatus

UserInputStatus 的公开协议结构。 / Public contract for user input status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending** | **bool** | 字段 pending / pending field。 | 
**question** | **str** | 字段 question / question field。 | [optional] 
**question_details** | **str** | 字段 questionDetails / question details field。 | [optional] 
**options** | **List[str]** | 字段 options / options field。 | [optional] 
**multiple** | **bool** | 字段 multiple / multiple field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.user_input_status import UserInputStatus

# TODO update the JSON string below
json = "{}"
# create an instance of UserInputStatus from a JSON string
user_input_status_instance = UserInputStatus.from_json(json)
# print the JSON string representation of the object
print(UserInputStatus.to_json())

# convert the object into a dict
user_input_status_dict = user_input_status_instance.to_dict()
# create an instance of UserInputStatus from a dict
user_input_status_from_dict = UserInputStatus.from_dict(user_input_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


