#python
def mais() :
    n1 = int(input("primeiro numero:"))
    n2 = int(input("segundo numero:"))
    print("o resultado é:", n1 + n2)
def menos() :
    n1 = int(input("primeiro numero:"))
    n2 = int(input("segundo numero:"))
    print("o resultado é:", n1 - n2)
def div() :
    n1 = int(input("primeiro numero:"))
    n2 = int(input("segundo numero:"))
    print("o resultado é:", n1 / n2)
def vezes () :
    n1 = int(input("primeiro numero:"))
    n2 = int(input("segundo numero:"))
    print("o resultado é:", n1 * n2)
perg = input("""
escolha a operação:
1. adisão
2. subtração
3. divisão
4. multiplicação
""")
if perg == "1" :
    mais()
elif perg == "2" :
    menos()
elif perg == "3" :
    div()
elif perg == "4" :
    vezes()
else :
    print("Opção invalida")

import calculadora
