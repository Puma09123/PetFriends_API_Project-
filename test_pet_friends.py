import unittest
from api import get_api_key, get_pets_list
from settings import valid_email, valid_password


class TestPetFriendsAPI(unittest.TestCase):

    def setUp(self):
        response = get_api_key(valid_email, valid_password)
        self.auth_key = response.json()["key"]

    # 1. Проверка получения ключа
    def test_get_api_key_valid_user(self):
        response = get_api_key(valid_email, valid_password)
        self.assertEqual(response.status_code, 200)
        self.assertIn("key", response.json())

    # 2. Получение списка всех питомцев
    def test_get_all_pets_valid_key(self):
        response = get_pets_list(self.auth_key)
        self.assertEqual(response.status_code, 200)

    # 3. Получение питомцев с пустым фильтром
    def test_get_pets_empty_filter(self):
        response = get_pets_list(self.auth_key, "")
        self.assertEqual(response.status_code, 200)

    # 4. Получение питомцев с неверным ключом
    def test_get_pets_invalid_key(self):
        response = get_pets_list("invalid_key")
        self.assertNotEqual(response.status_code, 200)

    # 5. Проверка структуры ответа
    def test_pets_response_structure(self):
        response = get_pets_list(self.auth_key)
        self.assertIn("pets", response.json())

    # 6. Проверка типа данных pets
    def test_pets_is_list(self):
        response = get_pets_list(self.auth_key)
        self.assertIsInstance(response.json()["pets"], list)

    # 7. Повторный запрос списка питомцев
    def test_repeat_get_pets(self):
        response1 = get_pets_list(self.auth_key)
        response2 = get_pets_list(self.auth_key)
        self.assertEqual(response1.status_code, response2.status_code)

    # 8. Проверка ответа без авторизации
    def test_get_pets_no_auth(self):
        response = get_pets_list("")
        self.assertNotEqual(response.status_code, 200)

    # 9. Проверка Content-Type
    def test_get_pets_content_type(self):
        response = get_pets_list(self.auth_key)
        self.assertIn("application/json", response.headers["Content-Type"])

    # 10. Проверка что список может быть пустым
    def test_pets_list_can_be_empty(self):
        response = get_pets_list(self.auth_key, "my_pets")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
