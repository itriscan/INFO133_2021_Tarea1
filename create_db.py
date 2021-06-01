import collections
from pymongo import MongoClient

dbUrl = MongoClient("mongodb://localhost", 27017)

db= dbUrl['FuSA']

collections1 = db["Usuarios"]
collections1.insert_one({"nombre":"aaaaa","apellido":"asdasdas","Rut":12345678-9})