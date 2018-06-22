import numpy as np

file = open("listaDeFilmes.txt", "r")

possiveisFilmes = []
filmesPreferidos = ["Whiplash", "Inglourious Basterds"]


txt = [] #array com todos os filmes e suas recomendacoes (possui repeticoes)
movies = [] #array com todos os filmes (nao possui repeticoes)
CONST = 12 #numero de filmes recomendados por cada filme
for line in file:               # le todas as linhas do arquivo
    aux = line[:-1]             # e adiciona os filmes nos dois
    txt.append(aux)             # vetores, verificando se ele
    if aux not in movies:       # ja esta contido no vetor movies,
        movies.append(aux)      # pois neste nao ha repeticoes

tamanho = len(movies)
file.close()

matrix = np.zeros((tamanho,tamanho)) #cria a matriz de transformacao

#debug
#for i in range(0, len(txt), CONST+1):
#    print(txt[i])
#    for j in range(i+1, i+CONST+1):
#        print(txt[j])
#    print("-------")

#relaciona cada filme com suas recomendacoes
for i in range(0, len(txt), CONST+1):
    for j in range(i+1, i+CONST+1):
        matrix[movies.index(txt[j])][movies.index(txt[i])] = (1/CONST)
        if txt[i] in filmesPreferidos and txt[j] not in possiveisFilmes and txt[j] not in filmesPreferidos:
            possiveisFilmes.append(txt[j])

for j in range(tamanho):                # verifica se algum filme nao
    soma = 0                            # recomenda nenhum outro (seu
    for i in range(tamanho):            # vertice nao liga nenhum outro)
        soma = soma + matrix[i][j]      # e, caso nao recomende, faca-o
    if soma == 0:                       # recomendar todos os outros
        for a in range(tamanho):        # (para que sua importancia nao
            matrix[a][j] = 1/tamanho    # seja toda jogada fora, ela eh
                                        # distribuida igualmente entre
                                        # todos os outros

#debug
#print(movies)
#for i in range(tamanho):
#    print(matrix[i])

v = np.full(tamanho, 1/tamanho) # cria um vetor inicial com o mesmo valor inicial para todos os filmes 


A = matrix                      # cria uma mtriz A = a matriz
result = A@v                    # de transformacao, eleva a 10
for i in range(10):             # (o suficiente para convergir)
    result = A@v                # e multiplica pelo vetor v
    #print(i, " => ", result)   #
    A = A@matrix                #



mov2rank = {}                               # cria um map juntando cada
for i in range(tamanho):                    # filme ao seu rank final
    if (result[i] != 0):                    # para facilitar a ordenacao
        #print(movies[i], " => ", result[i])#
        mov2rank[movies[i]] = result[i]     #

mov2rank = sorted(mov2rank.items(), key=lambda x: x[1]) # ordena o map dos filmes, do mais recomendado para o menos recomendado
mov2rank.reverse()
#print(mov2rank)
#print(filmesPreferidos)
#print(possiveisFilmes)

maximo = 5
listados = 0
if not possiveisFilmes:
    print("Entre todos os filmes listados, os", maximo, "mais recomendados sao:")
else :
    print("Baseado em seus filmes preferidos, os", maximo, "mais recomendados para voce sao:")
for (k,v) in mov2rank:
    if (k in possiveisFilmes or not possiveisFilmes) and listados < maximo:
        print(k)
        listados += 1

print(len(movies))