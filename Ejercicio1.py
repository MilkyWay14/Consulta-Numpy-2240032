# 2240032 - Daniver Franchesco Hernandez Acero
# Un array de 30 elementos (los 30 candidatos) en que el valor guardado en los elementos corresponde a los votos obtenidos
import numpy as np

# Se genera un array de 30 elementos con números aleatorios
candidatos = np.random.rand(30)

# La suma de todos los elementos se iguala a 5000
candidatos = candidatos / np.sum(candidatos) * 5000

# 2240032 - Daniver Franchesco Hernandez Acero
# Se pasan a entero y se ajusta el último número para que la suma sea 5000
candidatos = np.round(candidatos).astype(int)
candidatos[-1] = 5000 - np.sum(candidatos[:-1])

#Se genera un array con la identifiación de cada candidato
id_candidatos = np.arange(1, 31)

#Se genera una matriz con id y votos
matriz = np.column_stack((id_candidatos, candidatos))

#Se ordena de mayor a menor
matriz = sorted(matriz, key=lambda x: x[1], reverse=True)

print("Lista con candidatos ordenados por votos")
print("Candidato | Votos\n")
for candidato, votos in matriz:
    print(f"{candidato:9} | {votos:5}")

print("\nTotal de votos: ", np.sum(candidatos))
