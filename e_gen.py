'''VISUALIZAÇÃO: genoma bacteria x genoma humano'''

'''definindo entradas, alternando os arquivos |bacteria.fasta| e |human.fasta|'''
#entrada = open("bacteria.fasta").read()
entrada = open("human.fasta").read()
#saida = open("bacteria.html", "w")
saida = open("human.html", "w")

'''definindo contador'''
cont = {}

'''loop com formação de pares DNA'''
for i in ['A', 'T', 'C', 'G']:
    for h in ['A', 'T', 'C', 'G']:
        cont[i+h] = 0

'''correção de quebra de linha'''
entrada = entrada.replace("\n","")

'''loop para preenchimento da entrada'''
for k in range(len(entrada)-1):
    cont[entrada[k]+entrada[k+1]] += 1

#formação do arquivo HTML

saida.write("<div>")

c = 1
for d in cont:
    transparencia = cont[d]/max(cont.values())
    saida.write("<div style = 'width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0,0,0,"+str(transparencia)+"')>"+d+"</div>")
    
    if c%4 == 0:
        saida.write("<div style = 'clear:both'></div>")
    c+=1

saida.close()