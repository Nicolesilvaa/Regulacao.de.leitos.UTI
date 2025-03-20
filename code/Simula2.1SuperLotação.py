#Simulador 
import random, time
import cLeito
import cPacientes
import Gerenciador

#Segundo caso de teste: Testando superlotação

nPacientes = int(input("Olá! Digite a capacidade pacientes que seu hospital suporta atualmente "))
print()

Hospital1 = Gerenciador.Gerenciador_Leitos()
demandaExtra = nPacientes + 20

for x in range(demandaExtra):
    Hospital1.inserir_Ordenado(Hospital1.Fila_de_Espera,cPacientes.Paciente())


for x in range(nPacientes):
    Hospital1.inserir_leito(cLeito.cLeito())


print(Hospital1)

print(" ------------------------------------------------- Vinculando pacientes  -------------------------------------------------- \n ")
for i in range(demandaExtra):
    Hospital1.vincular_Espera()
    print()

print(Hospital1.imprimir_Espera())


print(Hospital1)

contador = 0
limite= 1

while contador < limite:

    for i in range(20):
        leito=cLeito.cLeito()
        Hospital1.inserir_leito(leito)
        print(f"Leito Disponível: {leito}")

    if Hospital1.len_Espera() == 0:
        contador += 1 

    print()

    print(" ------------------------------------------------- Vinculando pacientes  -------------------------------------------------- \n ")
    for i in range(10):
        Hospital1.vincular_Espera()
        for x in range(demandaExtra):
            Hospital1.inserir_Ordenado(Hospital1.Fila_de_Espera,cPacientes.Paciente())

    print()
    
    print(Hospital1)
    print(Hospital1.imprimir_Espera())
    time.sleep(1)

    
    
