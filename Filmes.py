filmes = ['Os vingadores', 'HP', 'Liga da Justiça', 'Animais fantastico', 'Planeta dos macacos', 'Lagoa azul', 'Um amor para recordar']
print(filmes)
print()
filmes.append('Esqueceram de mim')
print(filmes)
print()
filmes_novos = ['O poderoso chefão', 'De volta para o futuro', 'Jojo rabbit', 'Superman']
filmes.extend(filmes_novos)
print()
print(filmes)
print()
filmes.sort()
print(filmes)
print()
filmes.reverse()
print(filmes)
print()
filmes.insert(1, 'Homem de ferro')
print(filmes)
print()
filmes.sort()
print()

filmes.remove('Superman')
print(filmes)
print()
filmes.pop(6)
# del filmes[:] - Apaga a Lista toda
del filmes [0:2]


print()
for filme in filmes:
    print(filme)

print(len(filmes))

print('Homem de ferro' in filmes)