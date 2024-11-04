#Inicialize uma lista de 20 números inteiros. Armazene
#os números pares em uma lista PAR e os números
#ímpares em uma lista IMPAR. Imprima as listas PAR
#e IMPAR.

impar=[]
par=[]

for i in range(0,20):
    c=int(input("digite os numeros impares ou pares"))
    if c % 2==0:
        par.append(c)
    else:
        impar.append(c)
    
print(f"listas dos impares {impar}")
print(f"listas dos pares {par}")

#e IMPAR. 6. Faça um programa que receba a temperatura média
#de cada mês do ano e armazene-as em uma lista.
#Em seguida, calcule a média anual das temperaturas
#e mostre a média calculada juntamente com todas as
#temperaturas acima da média anual, e em que mês
#elas ocorreram (mostrar o mês por extenso: 1 –
#Janeiro, 2 – Fevereiro, . . . ).
# Inicializa uma lista para armazenar as temperaturas médias de cada mês
temperaturas = []

# Nomes dos meses
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Lê a temperatura média de cada mês
for i in range(12):
    temperatura = float(input(f"Digite a temperatura média de {meses[i]}: "))
    temperaturas.append(temperatura)

# Calcula a média anual
media_anual = sum(temperaturas) / len(temperaturas)

# Exibe a média anual
print(f"\nA média anual das temperaturas é: {media_anual:.2f}°C")

# Exibe as temperaturas acima da média anual
print("Temperaturas acima da média anual:")
for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"{meses[i]}: {temperaturas[i]:.2f}°C")




