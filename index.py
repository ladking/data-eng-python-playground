from postgresconfig import ConnectPostgres
from config import config
from database import queryBuilder
from models import UserModel
from udacity import exerciseOne

cursor =config.DBCursor



queryBuilder.CreateTable("users", UserModel)
queryBuilder.CreateTable("artists", exerciseOne.artistModel)
queryBuilder.CreateTable("songs", exerciseOne.songsModel)
