import collections
from pymongo import MongoClient

dbUrl = MongoClient("mongodb://localhost")

db= dbUrl['FuSA']
