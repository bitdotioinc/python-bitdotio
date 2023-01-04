import unittest
from unittest.mock import Mock, patch

from bitdotio import bitdotio


class TestConnect(unittest.TestCase):
    token = "v2_testtoken"

    def setUp(self) -> None:
        self.b = bitdotio(self.token)

    def test_min_max_conn_validation(
        self,
    ) -> None:
        test_cases = [(-1, 0), (0, -1), (0, 0), (1, 0)]
        for min_conn, max_conn in test_cases:
            with self.assertRaises(ValueError):
                bitdotio(self.token, min_conn=min_conn, max_conn=max_conn)

    @patch("bitdotio._bitdotio._BitV2._create_pool")
    def test_connect(self, mock_create_pool: Mock) -> None:
        db_1, db_2 = "my/db1", "my/db2"
        with self.b.pooled_connection(db_1):
            pass

        # get/put should be called and there should be one pool after connecting once
        self.assertEqual(len(self.b._pools), 1)
        mock_create_pool.return_value.getconn.assert_called_once()
        mock_create_pool.return_value.putconn.assert_called_once()
        # validate that connections are exposed inside an internal context manager
        mock_create_pool.return_value.getconn.return_value.__exit__.assert_called_once()

        mock_create_pool.return_value.getconn.reset_mock()
        mock_create_pool.return_value.putconn.reset_mock()
        with self.b.pooled_connection(db_1):
            pass

        # get/put should be called and there should be one pool after connecting to the
        # same database the second time.
        self.assertEqual(len(self.b._pools), 1)
        mock_create_pool.return_value.getconn.assert_called_once()
        mock_create_pool.return_value.putconn.assert_called_once()
        mock_create_pool.return_value.getconn.return_value.__exit__.assert_called_once()

        mock_create_pool.return_value.getconn.reset_mock()
        mock_create_pool.return_value.putconn.reset_mock()
        with self.b.pooled_connection(db_2):
            pass

        # get/put should be called and there should be two pools after connecting to
        # the second database.
        self.assertEqual(len(self.b._pools), 2)
        mock_create_pool.return_value.getconn.assert_called_once()
        mock_create_pool.return_value.putconn.assert_called_once()
        mock_create_pool.return_value.getconn.return_value.__exit__.assert_called_once()

    @patch("bitdotio._bitdotio._BitV2._create_pool")
    def test_cursor(self, mock_create_pool: Mock) -> None:
        db_1, db_2 = "my/db1", "my/db2"
        with self.b.pooled_cursor(db_1):
            pass

        # get/put should be called and there should be one pool after connecting once
        self.assertEqual(len(self.b._pools), 1)
        mock_create_pool.return_value.getconn.assert_called_once()
        mock_create_pool.return_value.putconn.assert_called_once()
        # validate that connections are exposed inside an internal context manager
        mock_create_pool.return_value.getconn.return_value.__exit__.assert_called_once()

        mock_create_pool.return_value.getconn.reset_mock()
        mock_create_pool.return_value.putconn.reset_mock()
        with self.b.pooled_cursor(db_1):
            pass

        # get/put should be called and there should be one pool after connecting to the
        # same database the second time.
        self.assertEqual(len(self.b._pools), 1)
        mock_create_pool.return_value.getconn.assert_called_once()
        mock_create_pool.return_value.putconn.assert_called_once()
        mock_create_pool.return_value.getconn.return_value.__exit__.assert_called_once()

        mock_create_pool.return_value.getconn.reset_mock()
        mock_create_pool.return_value.putconn.reset_mock()
        with self.b.pooled_cursor(db_2):
            pass

        # get/put should be called and there should be two pools after connecting to
        # the second database.
        self.assertEqual(len(self.b._pools), 2)
        mock_create_pool.return_value.getconn.assert_called_once()
        mock_create_pool.return_value.putconn.assert_called_once()
        mock_create_pool.return_value.getconn.return_value.__exit__.assert_called_once()
