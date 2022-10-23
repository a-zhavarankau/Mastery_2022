import pytest
from report import DataFormatter, WriterCSV, WriterJSON, WriterToFormat


@pytest.fixture
def get_all_users():
    users = [{"name": "Jimmy",
              "surname": "McGill",
              "salary": 9000,
              "currency": "USD",
              "taxes": [{"code": "federal", "percentage": 13.5},
                        {"code": "property", "percentage": 10},
                        {"code": "state", "percentage": 15}]
              },
             {"name": "Michael",
              "surname": "Ermantraut",
              "salary": 15000,
              "currency": "USD",
              "taxes": [{"code": "federal", "percentage": 13.5},
                        {"code": "state", "percentage": 15}]
              },
             {"name": "Ignacio",
              "surname": "Varga",
              "salary": 7000,
              "currency": "USD",
              "taxes": [{"code": "federal", "percentage": 13.5},
                        {"code": "state", "percentage": 15}]
              }]
    return users


@pytest.fixture
def filename():
    file_name = "test_file"
    return file_name


@pytest.fixture
def df(get_all_users):
    return DataFormatter(get_all_users)


@pytest.fixture
def writer_csv(filename):
    return WriterCSV(filename)


@pytest.fixture
def writer_json(filename):
    return WriterJSON(filename)


@pytest.fixture
def writer_to_format(filename):
    return WriterToFormat(filename)


@pytest.fixture
def get_one_user(get_all_users):
    return get_all_users[0]


@pytest.fixture
def get_another_user(get_all_users):
    return get_all_users[1]


@pytest.fixture
def get_expected_data():
    expected_data = [
        ['Jimmy', 'McGill', 9000, 'USD', 1215.0, 1350.0, 900.0, 5535.0],
        ['Michael', 'Ermantraut', 15000, 'USD', 2025.0, 2250.0, 0, 10725.0]
    ]
    return expected_data


@pytest.fixture
def get_formatted_data():
    formatted_data = [
        {'name': 'Jimmy', 'surname': 'McGill', 'salary': 9000, 'currency': 'USD',
         'federal_tax': 1215.0, 'state_tax': 1350.0, 'property_tax': 900.0,
         'salary_after_tax': 5535.0},
        {'name': 'Michael', 'surname': 'Ermantraut', 'salary': 15000, 'currency': 'USD',
         'federal_tax': 2025.0, 'state_tax': 2250.0, 'property_tax': 0,
         'salary_after_tax': 10725.0},
        {'name': 'Ignacio', 'surname': 'Varga', 'salary': 7000, 'currency': 'USD',
         'federal_tax': 945.0, 'state_tax': 1050.0, 'property_tax': 0,
         'salary_after_tax': 5005.0}
    ]
    return formatted_data
