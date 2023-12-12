from postgresconfig import ConnectPostgres
class _Config():
    def __init__(self):
        self.db_params = {
            "host":"localhost",
            "password":"postgres",
            "user": "postgres",
            "port": 5432,
            "database":"udacity"
         }
        self.DBCursor = ConnectPostgres(self.db_params)


config = _Config()