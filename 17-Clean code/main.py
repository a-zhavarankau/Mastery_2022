from report import WriterCSV, WriterJSON
from report import FileCreater


if __name__ == '__main__':
    users = [
        {
            "name": "Jimmy",
            "surname": "McGill",
            "salary": 9000,
            "currency": "USD",
            "taxes": [
                {
                    "code": "federal",
                    "percentage": 13.5
                },
                {
                    "code": "property",
                    "percentage": 10
                },
                {
                    "code": "state",
                    "percentage": 15
                }
            ],
        },
        {
            "name": "Michael",
            "surname": "Ermantraut",
            "salary": 15000,
            "currency": "USD",
            "taxes": [
                {
                    "code": "federal",
                    "percentage": 13.5
                },
                {
                    "code": "state",
                    "percentage": 15
                }
            ],
        },
        {
            "name": "Ignacio",
            "surname": "Varga",
            "salary": 7000,
            "currency": "USD",
            "taxes": [
                {
                    "code": "federal",
                    "percentage": 13.5
                },
                {
                    "code": "state",
                    "percentage": 15
                }
            ],
        }
    ]

    creater = FileCreater()
    filename = "output"
    # Create file <filename>.json
    creater.get_file(users, WriterJSON, filename)
    # Create file <filename>.csv
    creater.get_file(users, WriterCSV, filename)

