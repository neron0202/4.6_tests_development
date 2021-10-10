import pytest as pytest
from yandex_folder_creation import create_folder

folder_status_data =[
    ('', '<Response [200]>'),
]

class TestYaFolderCreate:

    @classmethod
    def setup_class(cls):
        print('setup_class')

    def setup(self):
        print('setup')

    @pytest.mark.parametrize('token_ya, expected_result', folder_status_data)
    def test_create_folder(self, token_ya, expected_result):
        assert create_folder(token_ya) == expected_result, '200'



    def teardown(self):
        print('teardown')

    @classmethod
    def teardown_class(cls):
        print('teardown_class')
