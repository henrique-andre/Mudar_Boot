import json

# Variáveis que você deseja salvar
variaveis = {
    "sistema1": ['    '],  # Coloque o nome da máquina do primeiro boot ex: "BOT - TOTVS - 18910/SP"
    "idso1": ['    '],  # Coloque aqui o identificador(bcdedit) do boot 01
    "sistema2": ['    '],  # Coloque o nome da máquina do segundo boot ex: "BOT - LINX - 18921/SP"
    "idso2": ['    ']  # Coloque aqui o identificador(bcdedit) do boot 02
}

# Salvar as variáveis em um arquivo JSON
with open('variaveis.json', 'w') as f:
    json.dump(variaveis, f, indent=4)
