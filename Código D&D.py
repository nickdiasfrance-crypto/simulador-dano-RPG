# -*- coding: utf-8 -*-

"""

import random
import matplotlib.pyplot as plt
#1 Definindo o dado (D12) e o modificador
dano_base=12
modificador=5
simulacoes=1000 # vamos simular 1000 ataques

resultado=[]

#2 O Loop (A mágica do computador)
for i in range(simulacoes):
 dado=random.randint(1,dano_base)
 dano_total= dado + modificador
 resultado.append(dano_total)

#3 Calculando a média
media= sum(resultado)/len(resultado)
print(f"Dano médio após{simulacoes} ataques:{media}")

#4 Criando um gráfico simples
plt.hist(resultado,bins=10,color='red',edgecolor='black')
plt.title('Distribuição de Dano')
plt.xlabel('Dano Final')
plt.ylabel('Frequência')
plt.show()

from google.colab import drive
drive.mount('/content/drive')
