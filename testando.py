import json

data = [
    {
        "Nome":"Fulano",
        "Idade":20,
        "e-mail":"fulano@mail.com"
    },
    {
        "Nome":"Ciclano",
        "Idade":15,
        "e-mail":"ciclano@mail.com"
    }
]

with open("clientes.json", "w") as file_cliente:
    json.dump(data, file_cliente)