import numpy as np

participantes  = [{"nome": "ana" ,
                    "localizacao" : "brasil" ,
                    "afiliacao" : "universidade A" ,
                    "interesses" : ["fisica" , "astronomia"]
                    },
                    {"nome": "samara" ,
                    "localizacao" : "EUA" ,
                    "afiliacao" : "universidade B" ,
                    "interesses" : ["matematica" , "astronomia"]
                    },
                    {"nome": "emerson" ,
                    "localizacao" : "paulo_lopes" ,
                    "afiliacao" : "universidade C" ,
                    "interesses" : ["geografia" , "astronomia"]
                    },
                    {"nome": "rebeca" ,
                    "localizacao" : "brasil" ,
                    "afiliacao" : "universidade A" ,
                    "interesses" : ["fisica" , "astronomia"]
                    }, ]
regioes = set(participante["localizacao"] for participante in participantes)

afiliacoes = {}

for participante in participantes:

    afiliacao = participante["afiliacao"]

    if afiliacao not in afiliacoes:

        afiliacoes[afiliacao] = []

    afiliacoes[afiliacao].append(participante["nome"])

areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante["interesses"]])

interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)

areas_mais_popular = interesses_unicos[np.argmax(contagem)]

print("Regiões dos participantes:", regioes)

print("afiliacoes dos participantes:")

for afiliacao, nome in afiliacoes.items():

    print(f"{afiliacao}: {', '.join(nome)}")
    
print("Área de interesse mais popular:" , areas_mais_popular)