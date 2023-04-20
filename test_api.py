import requests


class TestModel:
    def __set_task_id(self, set_url, set_path_to_create, set_create_payload):
        task_id = requests.put(set_url+set_path_to_create, json=set_create_payload).json()["task"]["task_id"]
        return task_id

    def get_get_response(self, set_url, set_path_to_create, set_create_payload):
        task_id = self.__set_task_id(set_url, set_path_to_create, set_create_payload)
        response = requests.get(f'https://todo.pixegami.io/get-task/{task_id}')
        return response

    def get_post_response(self, set_create_payload, set_url, set_path_to_create):
        response = requests.put(set_url + set_path_to_create, json=set_create_payload)
        return response

    def test_create(self, set_url, set_create_payload, set_path_to_create, set_expected_headers):
        response = requests.put(set_url + set_path_to_create, json=set_create_payload)
        actual_headers = (
            response.headers['Content-Length'],
            response.headers['Connection'],
            response.headers['X-Cache']
        )
        assert response.status_code == 200
        assert actual_headers == set_expected_headers

    def test_get(self, set_url, set_path_to_get, set_path_to_create, set_create_payload):
        response = self.get_get_response(set_url, set_path_to_create, set_create_payload)
        assert response.status_code == 200
        assert response.json()["is_done"] is False
        assert len(response.json()) > 0

    def test_put(self, set_url, set_put_payload, set_create_payload, set_path_to_create):
        response = requests.put(set_url+"/update-task", json=set_put_payload)
        self.get_post_response(set_create_payload, set_url, set_path_to_create)
        assert response.json()["updated_task_id"] == "string4"
        assert response.status_code == 200

    def test_delete(self, set_url,set_path_to_create, set_create_payload, set_path_to_delete, set_path_to_get):
        task_id = self.__set_task_id(set_url, set_path_to_create, set_create_payload)
        response = requests.delete(set_url+set_path_to_delete+task_id)
        self.get_post_response(set_create_payload, set_url, set_path_to_create)
        assert response.status_code == 200
        requests.delete(set_url+set_path_to_delete+task_id)
        assert self.get_get_response(set_url, set_path_to_create, set_create_payload).status_code == 404
