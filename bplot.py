'''VISUALIZAÇÃO: boxplot ou diagrama de caixa'''
import matplotlib.pyplot as plt
import random

vetor=[]

for i in range(100):
	nlt = random.randint(0,50)
	vetor.append(nlt)

plt.boxplot(vetor)
plt.show()