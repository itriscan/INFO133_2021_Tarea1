import collections
from pymongo import MongoClient

dburl = MongoClient("mongodb://localhost", 27017)

db= dburl['FuSA']
