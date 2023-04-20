import pytest


@pytest.fixture
def fixture_dict():
    dict = {"set_create_payload":{
  "content": "string1",
  "user_id": "string2",
  "task_id": "string3",
  "is_done": False
},"set_put_payload": {
  "content": "string7",
  "user_id": "string5",
  "task_id": "string4",
  "is_done": True
}, "set_expected_headers": ('159', 'keep-alive', 'Miss from cloudfront'),
    "set_url": "https://todo.pixegami.io/", "set_path_to_delete": "/delete-task/",
    "set_path_to_get": "/get-task/", "set_path_to_create": "/create-task"}
    return dict
