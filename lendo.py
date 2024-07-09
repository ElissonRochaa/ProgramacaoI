import json

data = []

try:
    with open("clientes.json", 'r') as file_clientes:
        data = json.load(file_clientes)
    
except FileNotFoundError as e:
    print("Arquivo não existe...")
except Exception as e:
    print("Ocorreu algum erro...")

print(data)