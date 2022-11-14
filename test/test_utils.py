import unittest

from bitdotio.utils import validate_database_name, validate_token


class TestUtils(unittest.TestCase):
    def test_validate_token_ok(self) -> None:
        validate_token("v2_testtoken")

    def test_validate_token_error(self) -> None:
        test_cases = ["v2_", "v1_testtoken", "v2__.--_--", "v2testtoken", "testtoken"]
        for test_case in test_cases:
            with self.assertRaises(ValueError):
                validate_token(test_case)

    def test_validate_database_name_ok(self) -> None:
        validate_database_name("my/db")
        validate_database_name("m/d")
        validate_database_name("my/db/with/some/slashes")
        validate_database_name("my/db/with.some+other$things")

    def test_validate_database_name_error(self) -> None:
        test_cases = [
            "/mydb",
            "mydb",
            "myExtremelyLongUserNameWhichIsDefinitelyWayTooLong/db",
            "me/myExtremelyLongDatabaseNameWhichIsDefinitelyWayTooLong",
            "-/db",
            "./db",
            "me/",
        ]
        for test_case in test_cases:
            with self.assertRaises(ValueError):
                validate_database_name(test_case)
