from typing import Union, Dict
import csv
import json
import os
import pytest
from pytest_lazyfixture import lazy_fixture
from report import DataFormatter, FileCreater, WriterToFormat


@pytest.mark.parametrize("user, tax_name, expected_result",
                         [(lazy_fixture("get_one_user"), "federal", 1215.0),
                          (lazy_fixture("get_one_user"), "common", 0),
                          (lazy_fixture("get_one_user"), 88, 0),
                          (lazy_fixture("get_one_user"), "", 0)])
def test_get_user_tax_val(user: Dict, tax_name: str, expected_result: Union[int, float]):
    assert DataFormatter.get_user_tax_val(user, tax_name) \
           == expected_result


def test_get_field_names(df):
    field_names = ['name', 'surname', 'salary', 'currency',
                   'federal_tax', 'state_tax', 'property_tax',
                   'salary_after_tax']
    assert df.get_field_names() == field_names


def test_get_tax_values(df, get_one_user, get_another_user, get_expected_data):
    assert df.get_tax_values(get_one_user) == get_expected_data[0][-4:-1]
    assert df.get_tax_values(get_another_user) == get_expected_data[1][-4:-1]


def test_get_user_data(df, get_one_user, get_another_user, get_expected_data):
    assert df.get_user_data(get_one_user) == get_expected_data[0]
    assert df.get_user_data(get_another_user) == get_expected_data[1]


def test_format_data_to_send(df, get_formatted_data):
    assert df.format_data_to_send() == get_formatted_data


def test_prepare_data_to_store_parent(get_all_users, writer_to_format):
    assert writer_to_format.prepare_data_to_store(get_all_users) is None
    assert writer_to_format.write_data_to_file(get_all_users) is None


def test_prepare_data_to_store_csv(get_formatted_data, writer_csv):
    result = writer_csv.prepare_data_to_store([get_formatted_data[0]])
    expected_result = [
        ['Name', 'Surname', 'Salary', 'Currency', 'Federal tax', 'State tax',
         'Property tax', 'Salary after tax'],
        ['Jimmy', 'McGill', 9000, 'USD', 1215.0, 1350.0, 900.0, 5535.0]
    ]
    assert result == expected_result


def test_write_data_to_file_csv(mocker, get_formatted_data, writer_csv, filename):
    # Mocking the function 'WriterCSV.prepare_data_to_store'
    def fake_function(self, input_data):
        data = [["data from"], ["mocking function"]]
        return data

    mocker.patch("report.WriterCSV.prepare_data_to_store", fake_function)

    writer_csv.write_data_to_file(get_formatted_data)
    with open(f"{filename}.csv", encoding="utf-8") as file:
        reader = csv.reader(file)
        result = list(reader)
    os.remove(f"{filename}.csv")
    expected_result = [['data from'], [], ['mocking function'], []]
    assert result == expected_result


def test_prepare_data_to_store_json(get_formatted_data, writer_json):
    assert writer_json.prepare_data_to_store(get_formatted_data) == get_formatted_data


def test_write_data_to_file_json(writer_json, filename):
    input_data = [{"One": 1, "Two": 2}]
    writer_json.write_data_to_file(input_data)
    with open(f"{filename}.json", encoding="utf-8") as file:
        result = json.load(file)
    expected_result = [{'One': 1, 'Two': 2}]
    os.remove(f"{filename}.json")
    assert result == expected_result


def test_create_file(get_all_users):
    assert FileCreater().create_file(get_all_users, WriterToFormat, "out.csv") is None
