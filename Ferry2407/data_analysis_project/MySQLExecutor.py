import mysql.connector
from mysql.connector import Error
import time
import csv

class MySQLExecutor:
    def __init__(self, host, user, password, database, csv_file_path, query_file_path):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.csv_file_path = csv_file_path
        self.query_file_path = query_file_path

    def execute_sql_from_file(self):
        connection = None
        cursor = None
        try:
            # Establish the connection
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if connection.is_connected():
                cursor = connection.cursor()
                with open(self.query_file_path, 'r') as file:
                    sql = file.read()
                # Execute each query in the file
                for query in sql.split(';'):
                    query = query.strip()
                    if query:
                        start_time = time.time()  # Record the start time
                        try:
                            cursor.execute(query)
                            # Handle different types of queries
                            if query.lower().startswith('select') or query.lower().startswith('show'):
                                # Fetch and print results for SELECT and SHOW queries
                                results = cursor.fetchall()
                                columns = [i[0] for i in cursor.description]
                                print(f"Results for query: {query}")
                                print(columns)
                                for row in results:
                                    print(row)
                                
                                # Write results to CSV
                                with open(self.csv_file_path, mode='w', newline='') as csv_file:
                                    writer = csv.writer(csv_file)
                                    writer.writerow(columns)  # Write column headers
                                    writer.writerows(results)  # Write data rows
                                print(f"Results saved to {self.csv_file_path}")
                            else:
                                # For other queries like CREATE, INSERT, etc.
                                print(f"Query executed successfully: {query}")
                            
                            connection.commit()
                        except Error as e:
                            print(f"Error executing query: {e}")
                        finally:
                            # Handle any remaining results
                            if connection.unread_result:
                                connection.handle_unread_result()
                        
                        end_time = time.time()  # Record the end time
                        execution_time = end_time - start_time
                        print(f"Query execution time: {execution_time:.2f} seconds")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None and connection.is_connected():
                connection.close()
                print("MySQL connection is closed")

if __name__ == "__main__":
    executor = MySQLExecutor(
        host='localhost',
        user='root',
        password='root',
        database='sm',
        csv_file_path='C:\\Users\\Administrator\\temp2\\2407-Ferry\\query_results.csv',
        query_file_path='C:\\Users\\Administrator\\temp2\\2407-Ferry\\queries.sql'
    )


    executor.execute_sql_from_file()