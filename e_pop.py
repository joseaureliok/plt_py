'''VISUALIZAÇÃO: Crescimento populacional entre ano 1980 e ano 2016, segundo o DataSUS'''

'''importação da biblioteca'''
import matplotlib.pyplot as plt

'''leitura do arquivo CSV'''
dados=open('populacao_brasileira.csv').readlines()

'''definindo variáveis |x e y| como (listas vazias)'''
x=[]
y=[]

'''criação do loop para preenchimento das variáveis'''
for i in range(len(dados)):
	if i !=0:
		linha = dados[i].split(";");
		x.append(int(linha[0]))
		y.append(int(linha[1]))

'''impressão do gráfico |PNG|'''
plt.scatter(x,y, marker= "^", color = "red")
plt.plot(x,y, linestyle=":", color = "k")
plt.bar(x,y, color="#CDBA96")
plt.title("DataSUS: Crescimento da população brasielira de 1980 a 2016")
plt.xlabel("Ano")
plt.ylabel("População (*100milhões)")
plt.legend()
plt.savefig("popDtSUS.png", dpi=300)