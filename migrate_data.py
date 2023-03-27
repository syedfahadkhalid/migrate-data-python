import pymysql
import logging
from configs import Config as conf
from sql import SQL as sql
import time


class MigrateData:
    def __init__(self):
        pass

    @staticmethod
    def get_connection():
        conn = pymysql.connect(host=conf.db_url, user=conf.db_username, password=conf.db_password,
                               database=conf.schema, port=conf.db_port, connect_timeout=5)
        return conn

    def get_all_batches(self, statement):
        logging.info(f'Loading Batches')

        start = conf.start
        end = conf.end
        temp = start + conf.batch_size

        sql_statements = self.prepare_sql_statements(statement, start, end, temp)

        logging.info(f'Total Statements Created: {str(len(sql_statements))}')
        return sql_statements

    def prepare_sql_statements(self, statement, start, end, temp):
        prepared_sql_statements = []
        while temp < end:
            stmt = statement % (start, temp)
            prepared_sql_statements.append(stmt)

            start = temp+1
            temp = start + conf.batch_size
        stmt = statement % (start, end)
        prepared_sql_statements.append(stmt)

        return prepared_sql_statements

    def migrate_data(self):
        migrate_stmts = self.get_all_batches(sql.migrate_sql())
        con = self.get_connection()
        lngth = len(migrate_stmts)
        with con.cursor() as cursor:
            for statement in migrate_stmts:
                cursor.execute(statement['stmt'])
                con.commit()
                time.sleep(60)
                lngth = lngth - 1
                logging.info(f'Executed, now remaing: {str(lngth)}')

