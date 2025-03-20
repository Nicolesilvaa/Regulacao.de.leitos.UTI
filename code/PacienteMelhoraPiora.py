import random
import cLeito
import cPacientes
import Gerenciador
import cFila

def determine_evento(idade):

    if idade < 11: 
        return "melhorou"

    elif idade <= 156: #Entre 1 e 13
        return random.choice(["melhorou", "morreu"])

    else:

        # Forçar para um evento mais grave: ou "morreu" ou "melhorou"
        if idade > 600:  # Para pacientes acima de 50 anos, maior chance de morrer
            return "morreu"
        else:
            eventos = ["melhorou", "sem mudança", "morreu"]
            return random.choice(eventos)  

def acompanhaPacientesNaFila(lista_pacientes, gerenciador):
  
    print("\n------------------------ Início da simulação de evolução dos pacientes na fila -------------------------\n")

    pacientes_para_remover = cFila.cFila()
    fila_auxiliar = cFila.cFila() 
    tamanho_fila = gerenciador.Fila_de_Espera.tamanho()
    
    for i in range(tamanho_fila):
        paciente = gerenciador.Fila_de_Espera.dequeue()
        evento = determine_evento(paciente.idade)

        print(f"Processando Paciente ID: {paciente.id}, Idade: {paciente.idadeEmAnos()}")

        if evento == "morreu":
            pacientes_para_remover.dequeue()
            print(f"Paciente {paciente.id} faleceu.\n")

        elif evento == "melhorou":
            pacientes_para_remover.dequeue()
            print(f"Paciente {paciente.id} melhorou.\n")

        else:
            fila_auxiliar.queue(paciente)
            print(f"Paciente {paciente.id} sem alteração de estado.\n")

        
    while not fila_auxiliar.empty():
        gerenciador.Fila_de_Espera.queue(fila_auxiliar.dequeue())  # Devolve os pacientes à fila original

    # Remover pacientes falecidos ou melhorados
    while not pacientes_para_remover.empty():
        paciente = pacientes_para_remover.dequeue()
        print(f"Removendo o paciente {paciente.id} da fila de espera.")


if __name__ == '__main__':

    nPacientes = int(input("Digite a capacidade de pacientes que seu hospital suporta atualmente: "))

    lista_pacientes = cFila.cFila()
    for i in range(nPacientes):

        paciente = cPacientes.Paciente()  
        lista_pacientes.queue(paciente)

    print(f"\n---------------------------Fila de espera inicial---------------------------\n {lista_pacientes}")
    
    gerenciador1 = Gerenciador.Gerenciador_Leitos()
    gerenciador1.Fila_de_Espera = lista_pacientes

    acompanhaPacientesNaFila(lista_pacientes,gerenciador1)

    print(f"\n----------------------Fila de espera final------------------------------------\n {gerenciador1.Fila_de_Espera()}")

