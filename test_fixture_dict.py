import requests


class TestModel:
    def __set_task_id(self, fixture_dict):
        task_id = requests.put("https://todo.pixegami.io/create-task", json=fixture_dict["set_create_payload"]).json()["task"]["task_id"]
        return task_id

    def get_get_response(self, fixture_dict):
        task_id = self.__set_task_id(fixture_dict["set_create_payload"])
        response = requests.get(f'https://todo.pixegami.io/get-task/{task_id}')
        return response

    def get_post_response(self, fixture_dict):
        response = requests.put(fixture_dict["set_url"] + fixture_dict["set_path_to_create"], json=fixture_dict["set_create_payload"])
        return response

    def test_create(self, fixture_dict):
        response = requests.put(fixture_dict["set_url"] + fixture_dict["set_path_to_create"], json=fixture_dict["set_create_payload"])
        actual_headers = (
            response.headers['Content-Length'],
            response.headers['Connection'],
            response.headers['X-Cache']
        )
        assert response.status_code == 200
        assert actual_headers == fixture_dict["set_expected_headers"]

    def test_get(self, fixture_dict):
        response = self.get_get_response(fixture_dict["set_create_payload"])
        assert response.status_code == 200
        assert response.json()["is_done"] is False
        assert len(response.json()) > 0

    def test_put(self, fixture_dict):
        response = requests.put(fixture_dict["set_url"]+"/update-task", json=fixture_dict["set_put_payload"])
        self.get_post_response(fixture_dict["set_create_payload"], fixture_dict["set_url"], fixture_dict["set_path_to_create"])
        assert response.json()["updated_task_id"] == "string4"
        assert response.status_code == 200

    def test_delete(self, fixture_dict):
        task_id = self.__set_task_id(fixture_dict["set_create_payload"])
        response = requests.delete(fixture_dict["set_url"]+fixture_dict["set_path_to_delete"]+task_id)
        self.get_post_response(fixture_dict["set_create_payload"], fixture_dict["set_url"], fixture_dict["set_path_to_create"])
        assert response.status_code == 200
        requests.delete(fixture_dict["set_url"]+fixture_dict["set_path_to_delete"]+task_id)
        assert self.get_get_response(fixture_dict["set_create_payload"]).status_code == 404
