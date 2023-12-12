from config import config

cur = config.DBCursor


class _QueryBuilder():

    def CreateTable(self, tablename, columns):
        query = "CREATE TABLE IF NOT EXIST"
        query += " " + tablename + "("

        for x in columns:
            columntype = self.ConvertTypes(columns[x])
            query += "{} {}, ".format(x, columntype)
        
        query = query.rstrip(", ")
        query += ")"
        print(query)


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