# def somaTudo(num1,num2,num3=0):
#     return num1+num2+num3

# print(somaTudo(num2=2, num1=3))
# print(somaTudo(2,3,4))
# #print(somaTudo(2,num2=3,4))


# lista = [x for x in [1,2,3,5] if x >2]
# lista.reverse()
# print(lista.pop())

# def funcao(*varArgs):
#     return [x+1 for x in varArgs if x < 2]
# print(funcao(1,2,3,4))

# def func(x):
#     return x*2
# f = [x+2 for x in range(0,6, 2)]
# print(func(f))

# # def funcao2(x=2, y):
# #     return x*y
# #print(funcao2(x=1,y=3))

# def verifica(var1):
#     return (not(not(var1>=3))) and (not(var1>4))

# print(verifica(3))
# print(verifica(0))
# print(verifica(-1))
# print(verifica(2))
# print(verifica(1))

def funcao(x,y,z):
    if x < 0:
        if y < 0:
            print("x < 0 and y < 0")
    elif z > 0:
        print("x > 0 and z > 0")

print(funcao(-1,2,4))

f = lambda i,j: [2*x for x in range(i,j)]
print(f(1,3))