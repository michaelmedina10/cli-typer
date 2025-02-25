from dataclasses import dataclass

import pandas as pd
import pymysql


@dataclass
class MySqlConnection:
    host: str
    user: str
    pmysql: str
    database: str
    port: int = 3306
    connection = None

    def __post_init__(self):
        self.port = int(self.port)

    def __enter__(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.pmysql,
                database=self.database,
                port=self.port,
                cursorclass=pymysql.cursors.DictCursor,
            )
            return self
        except pymysql.Error as e:
            print(f"Error to connect with MySql: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self, "connection"):
            self.connection.close()

    def execute_fetch(self, sql, params: tuple | None = None) -> pd.DataFrame:
        """
        Execute 'select query'.

        Args:
            sql (str): Query SQL
            params (tuple): parametros para query

        Returns:
            pd.DataFrame
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, params)
                result = cursor.fetchall()
                return pd.DataFrame(
                    result, columns=[col[0] for col in cursor.description]
                )
        except pymysql.Error as e:
            print(f"Error to fetch: {e}")
            return pd.DataFrame()

    def execute_dml(
        self, query: str, data: dict | list | None = None
    ) -> tuple[bool, str]:
        """
        Execute any DML instruction: 'insert, update, delete, truncate, etc'.

        Args:
            query (str): Query SQL
            data (dict| list): parameters of query

        Returns:
            bool: True to success False to some fail.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, data)
                self.connection.commit()
                return True, ""
        except pymysql.Error as e:
            print(f"DML Error: {e}")
            self.connection.rollback()
            return False, str(e)
