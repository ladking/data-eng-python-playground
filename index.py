from postgresconfig import ConnectPostgres
from config import config
from database import queryBuilder
from models import UserModel


cursor =config.DBCursor



queryBuilder.CreateTable("users", UserModel)