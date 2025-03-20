#Simulador 
import cLeito
import cPacientes
import Gerenciador
from PacienteMelhoraPiora import acompanhaPacientesNaFila

# Primeiro caso de teste: Criando pacientes e leitos e testando a probabilidade deles melhorarem ou baterem as botas na fila de espera
nPacientes = int(input("Olá! Digite a capacidade pacientes que seu hospital suporta atualmente "))
Hospital= Gerenciador.Gerenciador_Leitos()

for i in range(nPacientes):
    Hospital.inserir_leito(cLeito.cLeito())
    Hospital.inserir_Ordenado(Hospital.Fila_de_Espera, cPacientes.Paciente())
    
acompanhaPacientesNaFila(Hospital.Fila_de_Espera,Hospital)

#Testando o vincular Paciente que também tira o paciente da lista caso seja vinculado. Caso não seja vincualdo ele vai para a lista de espera.
print(Hospital)

print()
print("------------------------------------------------- Vinculando pacientes  -------------------------------------------------- \n")
for i in range(nPacientes):
    Hospital.vincular_Espera()

print()
print(f"Estado da Lista de Espera: \n {Hospital.imprimir_Espera()}")

print(Hospital)







