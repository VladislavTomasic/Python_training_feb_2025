
colectie=[100,200,300]

def scade_5(x):
    return x-5

print(list(map(scade_5,colectie)))


colectie =["100","200","300"]
print(list(map(int,colectie)))



#functia anonima
def putere(x):
    return x**2

print(list(map(putere,[2,3,4])))


print(list(map(lambda x:x**2,[2,3,4])))


ridicare_la_putere = lambda x:x**2
print(ridicare_la_putere(2))




fruits =["Apples", "Oranges", "Bananas","Tea"]
sorted(fruits)
print(sorted(fruits))


print(sorted(fruits,key=len))
print(sorted(fruits,key=len, reverse=True))