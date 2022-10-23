""" Module creates files in .CSV and .JSON formats.
    To create a file in additional format, just add a new class that
    inherits from 'WriterToFormat' and override its methods"""

import csv
import json
from typing import List, Dict, Union, Type


class WriterToFormat:
    def __init__(self, filename: str):
        self.filename = filename

    def prepare_data_to_store(self, input_data: List[Dict]):
        pass

    def write_data_to_file(self, input_data: List[Dict]):
        pass


class FileCreater:
    def get_file(self, data: List[Dict], handler: Type[WriterToFormat], filename: str) -> None:
        data_to_store = DataFormatter(data).format_data_to_send()
        handler(filename).write_data_to_file(data_to_store)


class WriterCSV(WriterToFormat):
    def prepare_data_to_store(self, input_data: List[Dict]) -> List[List]:
        data_to_store = []
        titles = [field_name.capitalize().replace("_", " ") for field_name in input_data[0].keys()]
        data_to_store.append(titles)
        for user in input_data:
            data_to_store.append(list(user.values()))
        return data_to_store

    def write_data_to_file(self, input_data: List[Dict]) -> None:
        data_to_store = self.prepare_data_to_store(input_data)
        with open(f"{self.filename}.csv", "w", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data_to_store)


class WriterJSON(WriterToFormat):
    def prepare_data_to_store(self, input_data: List[Dict]) -> List[Dict]:
        return input_data

    def write_data_to_file(self, input_data: List[Dict]):
        data_to_store = self.prepare_data_to_store(input_data)
        with open(f"{self.filename}.json", "w", encoding="utf-8") as file:
            json.dump(data_to_store, file)


class DataFormatter:
    def __init__(self, raw_data: List[Dict]):
        self.raw_data = raw_data

    @staticmethod
    def get_user_tax_val(user: Dict, tax_name: str) -> Union[int, float]:  # @staticmethod
        try:
            tax = [x["percentage"] for x in user["taxes"] if x["code"] == tax_name][0]
            tax_value = user["salary"] * tax / 100
            return tax_value
        except IndexError:
            return 0

    def get_field_names(self) -> List[str]:
        fields_except_taxes = [elem for elem in self.raw_data[0].keys() if elem != "taxes"]

        fields_taxes = []
        for user in self.raw_data:
            for elem in user["taxes"]:
                if elem["code"] not in fields_taxes:
                    fields_taxes.append(elem["code"])

        # Make correct sequence of tax names ("property" should be last)
        last_tax_name = "property"
        fields_taxes.remove(last_tax_name)
        fields_taxes.append(last_tax_name)
        fields_taxes = [name + "_tax" for name in fields_taxes]

        field_names = fields_except_taxes
        field_names.extend(fields_taxes)
        field_names.append("salary_after_tax")
        return field_names

    def get_tax_values(self, user: Dict) -> List[Union[int, float]]:
        list_of_taxes = self.get_field_names()[-4:-1]
        list_tax_values = [self.get_user_tax_val(user, tax[:-4]) for tax in list_of_taxes]
        return list_tax_values

    def get_user_data(self, user: Dict) -> List[Union[str, int, float]]:
        data_except_tax_values = [user[field] for field in user if field != "taxes"]
        tax_values = self.get_tax_values(user)
        salary_after_tax = user["salary"] - sum(tax_values)
        user_data = data_except_tax_values + tax_values + [salary_after_tax]
        return user_data

    def format_data_to_send(self) -> List[Dict]:
        field_names = self.get_field_names()

        all_user_data = []
        for user in self.raw_data:
            all_user_data.append(self.get_user_data(user))

        formatted_data = [dict(zip(field_names, user_data)) for user_data in all_user_data]
        return formatted_data
