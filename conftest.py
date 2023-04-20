import pytest


@pytest.fixture
def set_create_payload():
    payload_create = {
  "content": "string1",
  "user_id": "string2",
  "task_id": "string3",
  "is_done": False
}
    return payload_create
@pytest.fixture
def set_put_payload():
    payload_put = {
  "content": "string7",
  "user_id": "string5",
  "task_id": "string4",
  "is_done": True
}
    return payload_put


@pytest.fixture
def set_expected_headers():
    expected_headers = ('159', 'keep-alive', 'Miss from cloudfront')
    return expected_headers


@pytest.fixture
def set_url():
    url = "https://todo.pixegami.io/"
    return url


@pytest.fixture
def set_path_to_delete():
    path_to_delete = "/delete-task/"
    return path_to_delete


@pytest.fixture
def set_path_to_get():
    path_to_get = "/get-task/"
    return path_to_get


@pytest.fixture
def set_path_to_create():
    path_to_create = "/create-task"
    return path_to_create

