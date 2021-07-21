import collections
from pymongo import MongoClient

dbUrl = MongoClient("mongodb://localhost")

db= dbUrl['FuSA']

collection_archive = db['Archivos']
collections_type_of_font = db['tipos_de_fuentes']

new_archive = collection_archive.insert_one({
    "ID" : 1,
    "fecha_de_grabacion" : "mar 08 jun 2021",
    "ciudad" : "Coyhaique",
    "duracion" : "0:11",
    "formato" : ".wav",
    "Usuario" : {"RUT": 123456789,"nombre": "Nombre1", "apellido": "Apellido1"},
    "segmentos" : [{
        "ID":1,
        "formato": ".wav",
        
    }]
})

new_font = collections_type_of_font.insert_one({
    "tipo" : "lluvia",
    "archivo" : [1,1,1]

})