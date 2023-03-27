class SQL:

    def __init__(self):
        pass

    @staticmethod
    def migrate_sql():
        sql = "INSERT INTO table_name(col1,col1) \
               SELECT col1,col1 \
               FROM table_name2 \
               WHERE col_id between %s AND %s;"
        return sql
