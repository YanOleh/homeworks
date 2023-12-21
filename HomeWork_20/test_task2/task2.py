from function import load_db, change_user_data, add_new_user
from unittest.mock import patch
import unittest
import tempfile
import os
import json

class TestLoadDBFunction(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)

    def tearDown(self):
        os.remove(self.temp_file.name)

    def test_load_db_read(self):
        data = {'subscriber': [{'name': 'John', 'email': 'aaa@aaaa.com'}]}
        with open(self.temp_file.name, 'w') as f:
            json.dump(data, f)
        result = load_db(self.temp_file.name, 'r')
        self.assertEqual(result, data)

    def test_load_db_write_to_file(self):
        data = {'subscriber': [{'name': 'Alice', 'email': 'aaa@aaaa.com'}]}
        load_db(self.temp_file.name, 'w', data)
        with open(self.temp_file.name, 'r') as f:
            result = json.load(f)
        self.assertEqual(result, data)





class TestChangeUserDataFunction(unittest.TestCase):


    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)

    def tearDown(self):
        os.remove(self.temp_file.name)



    @patch('builtins.input', side_effect=['2'])
    def test_change_user_data_invalid_choice(self, mock_input):
        file_name = self.temp_file.name
        found_contacts = [{'phone_number': '123456789', 'first_name': 'John', 'last_name': 'Doe', 'city': 'City1'}]
        users = {'subscriber': found_contacts}
        change_user_data(2, found_contacts, users, file_name)
        self.assertEqual(users['subscriber'][0]['phone_number'], '123456789')

    @patch('builtins.input', side_effect=['2', '5'])
    def test_change_user_data_invalid_function(self, mock_input):
        file_name = self.temp_file.name
        found_contacts = [{'phone_number': '123456789', 'first_name': 'John', 'last_name': 'Doe', 'city': 'City1'}]
        users = {'subscriber': found_contacts}
        change_user_data(2, found_contacts, users, file_name)
        self.assertEqual(users['subscriber'][0]['phone_number'], '123456789')

    @patch('builtins.input', side_effect=['1', '1', '987654321'])
    def test_change_user_data_change_phone_number(self, mock_input):
        file_name = self.temp_file.name
        found_contacts = [{'phone_number': '123456789', 'first_name': 'John', 'last_name': 'Doe', 'city': 'City1'}]
        users = {'subscriber': found_contacts}
        change_user_data(2, found_contacts, users, file_name)
        self.assertEqual(users['subscriber'][0]['phone_number'], '987654321')

class TestAddNewUserFunction(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)

    def tearDown(self):
        os.remove(self.temp_file.name)

    @patch('builtins.input', side_effect=['John', 'Doe', 'City1', '123456789'])
    def test_add_new_user(self, mock_input):
        file_name = self.temp_file.name
        add_new_user(file_name)
        updated_data = load_db(file_name)
        self.assertEqual(len(updated_data['subscriber']), 1)
        new_user = updated_data['subscriber'][0]
        self.assertEqual(new_user['first_name'], 'John')
        self.assertEqual(new_user['last_name'], 'Doe')
        self.assertEqual(new_user['city'], 'City1')
        self.assertEqual(new_user['phone_number'], '123456789')



if __name__ == '__main__':
    unittest.main()



