import unittest
from unittest.mock import patch, MagicMock
from MySQLExecutor import MySQLExecutor
import pandas as pd
import os

class TestMySQLExecutor(unittest.TestCase):

    def __init__(self, methodName='runTest', host='', user='root', password='root', database='sm', csv_file_path='C:\\Users\\Administrator\\temp2\\2407-Ferry\\query_results.csv', query_file_path='C:\\Users\\Administrator\\temp2\\2407-Ferry\\queries.sql', report_path='C:\\Users\\Administrator\\SM_DataAnalysis\\Ferry2407\\data_analysis_project\\test_report\\test_report.csv'):
        super(TestMySQLExecutor, self).__init__(methodName)
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.csv_file_path = csv_file_path
        self.query_file_path = query_file_path
        self.report_path = report_path
        self.executor = MySQLExecutor(self.host, self.user, self.password, self.database, self.csv_file_path, self.query_file_path)

    def test_init(self):
        self.assertEqual(self.executor.host, self.host)
        self.assertEqual(self.executor.user, self.user)
        self.assertEqual(self.executor.password, self.password)
        self.assertEqual(self.executor.database, self.database)
        self.assertEqual(self.executor.csv_file_path, self.csv_file_path)
        self.assertEqual(self.executor.query_file_path, self.query_file_path)

    @patch('mysql.connector.connect')
    def test_execute_sql_from_file(self, mock_connect):
        # Mock the connection and cursor
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_connection.is_connected.return_value = True
        mock_cursor.fetchall.return_value = [('row1',), ('row2',)]
        mock_cursor.description = [('column1',), ('column2',)]

        # Mock reading the SQL file
        with patch('builtins.open', unittest.mock.mock_open(read_data='SELECT * FROM test;')):
            self.executor.execute_sql_from_file()

        # Assertions to check if the methods were called correctly
        mock_connect.assert_called_once_with(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        mock_cursor.execute.assert_called_once_with('SELECT * FROM test')
        mock_cursor.fetchall.assert_called_once()
        mock_connection.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()

def generate_test_report(report_path):
    # Run the tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestMySQLExecutor)
    result = unittest.TestResult()
    suite.run(result)

    # Collect test results
    test_results = []
    for test, err in result.errors:
        test_results.append({
            'test': str(test),
            'status': 'error',
            'details': err
        })
    for test, err in result.failures:
        test_results.append({
            'test': str(test),
            'status': 'failure',
            'details': err
        })
    for test in suite:
        if test not in [t[0] for t in result.errors] and test not in [t[0] for t in result.failures]:
            test_results.append({
                'test': str(test),
                'status': 'success',
                'details': ''
            })

    # Convert to DataFrame
    df = pd.DataFrame(test_results)

    # Save to CSV
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    df.to_csv(report_path, index=False)

if __name__ == '__main__':
    current_file_name = os.path.basename(__file__)
    report_path = f'C:\\Users\\Administrator\\SM_DataAnalysis\\Ferry2407\\data_analysis_project\\test_report\\{current_file_name}_report.csv'
    generate_test_report(report_path)