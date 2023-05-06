import pymongo
import pprint

# Cria a conexão com o MongoDB
connection = pymongo.MongoClient("Connection String")

db = connection.bank
collection = db.clients

# Lista de Documentos
new_clients = [{
            "agency": 1050,
            "name": "Joaquim Jose",
            "cpf": "999.999.999-99",
            "address": "Av Mal Tito, 7014",
            "account": ["cc", "115641"],
            "balance": 56755
            },
            {
            "agency": 1050,
            "name": "Roque Júnior",
            "cpf": "888.888.888-88",
            "address": "Rua Dunas de Miragaia, 512",
            "account": ["cp", "654651"],
            "balance": 984561
            },
            {
            "agency": 2000,
            "name": "Maria Lima",
            "cpf": "777.777.777-77",
            "address": "Rua Joaquim Jose, 1",
            "account": ["cp", "65465"],
            "balance": 654654
            },
            {
            "agency": 2000,
            "name": "Mathew Silva",
            "cpf": "666.666.666-66",
            "address": "Rua Maria de Lourdes, 17",
            "account": ["cc", "98451"],
            "balance": 1500
            }]


clients = db.clients
result = clients.insert_many(new_clients)
print(result.inserted_ids)


pprint.pprint(db.clients.find_one({"name": "Joaquim Jose"}))


for client in clients.find():
    pprint.pprint(client)


for client in clients.find({}).sort("name"):
    pprint.pprint(client)


for client in clients.find({"agency": 2000}):
    pprint.pprint(client)


for client in clients.find({"account": "cp"}):
    pprint.pprint(client)


for client in clients.find({"account": "cc"}):
    pprint.pprint(client)