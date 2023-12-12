from config import config
import psycopg2

cur = config.DBCursor


class _QueryBuilder():

    def CreateTable(self, tablename, columns):
        query = "CREATE TABLE IF NOT EXISTS"
        query += " " + tablename + " ("

        for x in columns:
            columntype = self.ConvertTypes(columns[x])
            query += "{} {}, ".format(x, columntype)
        
        query = query.rstrip(", ")
        query += ")"

        try:
            cur.execute(query)
        except psycopg2.Error as err:
            print(f"Error creating table {tablename} with error {err}")
            return


    def ConvertTypes(self, columntype):
        if columntype == "string":
            return "VARCHAR(50)"
        elif columntype == "int":
            return "INTEGER"
        elif columntype == "boolean":
            return "BOOLEAN"
            
        elif columntype == "DATE":
            return "TIMESTAMP"
            
        else:
            return columntype


queryBuilder = _QueryBuilder()