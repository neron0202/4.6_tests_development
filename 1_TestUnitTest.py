import pytest as pytest
from app import check_document_existance, get_doc_owner_name, add_new_doc

doc_existance_data = [("2207 876234", True),
                      ('27 89', False)
                      ]

doc_owner_name_data = [('2207 876234', 'Василий Гупкин'),
                       ('27 89', None)
                       ]

add_new_doc_data = [('89-555', 'INN', "Виталий Валов", "1", "1"),
                    ('124-66', 'passport', 'Гарри Поттер', '9', '9')]


class TestDocExistance:

    @classmethod
    def setup_class(cls):
        print('setup_class')

    def setup(self):
        print('setup')

    @pytest.mark.parametrize('input_doc_num, expected_result', doc_existance_data)
    def test_check_document_existance(self, input_doc_num, expected_result):
        assert check_document_existance(input_doc_num) == expected_result, 'Документ существует'

    def teardown(self):
        print('teardown')

    @classmethod
    def teardown_class(cls):
        print('teardown_class')


class TestGetOwnerName:

    @classmethod
    def setup_class(cls):
        print('setup_class')

    def setup(self):
        print('setup')

    @pytest.mark.parametrize('input_name, expected_result', doc_owner_name_data)
    def test_get_doc_owner_name(self, input_name, expected_result):
        assert get_doc_owner_name(input_name) == expected_result, 'Документ и его владелец найдены'

    def teardown(self):
        print('teardown')

    @classmethod
    def teardown_class(cls):
        print('teardown_class')


class TestAddNewDoc:

    @classmethod
    def setup_class(cls):
        print('setup_class')

    def setup(self):
        print('setup')

    @pytest.mark.parametrize('new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, expected_result', add_new_doc_data)
    def test_add_new_doc(self, new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, expected_result):
        assert add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number) == expected_result, 'Тест пройден'

    def teardown(self):
        print('teardown')

    @classmethod
    def teardown_class(cls):
        print('teardown_class')
