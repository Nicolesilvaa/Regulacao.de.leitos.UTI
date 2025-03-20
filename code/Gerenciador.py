import cFila as c
import cLeito as cl

# Estou criando uma classe para gerenciar os Pacientes e Leitos, ela seria a responsável por vincular e desvincular as duas classes(Paciente e Leito) e pela fila de espera.

class Gerenciador_Leitos:

    def __init__ (self):

        self.LeitosAdultos    = c.cFila()
        self.LeitosPediátricos= c.cFila()
        self.LeitosNeonatais  = c.cFila()

        self.Fila_de_Espera= c.cFila() #Aguardando contato
    
    def __str__(self):
        
        strLeitores =  " ------------------------------------------------- Leitos atuais --------------------------------------------------\n"
        strLeitores +=  f" Adulto: \n {(self.LeitosAdultos)}\n"
        strLeitores += f" Pediátrico: \n {(self.LeitosPediátricos)} \n"
        strLeitores += f" NeoNatal: \n {(self.LeitosNeonatais)} \n "
        strLeitores += f"Estado atual\n"
        strLeitores += f"Adulto:{self.len_Adulto()}, Pediátrico:{self.len_Pediatrico()}, NeoNatal:{self.len_Neonatal()}, Fila de Espera: {self.len_Espera()}.\n "

        #strLeitores += " \n ------------------------------------------------- Vinculando pacientes  #--------------------------------------------------"

        return strLeitores

    def len_Adulto(self):
        return (self.LeitosAdultos.tamanho())

    def len_Pediatrico(self):
        return (self.LeitosPediátricos.tamanho())

    def len_Neonatal(self):
        return (self.LeitosNeonatais.tamanho())
    
    def len_Espera(self):
        return (self.Fila_de_Espera.tamanho())
        
    def imprimir_Espera(self):

        print(" ------------------------------------------------- Estado atual da lista de espera --------------------------------------------------")
        return self.Fila_de_Espera
    
    def imprimir_LeitosAdultos(self):
        return self.LeitosAdultos
    
    def imprimir_LeitosPediátricos(self):
        return self.LeitosPediátricos
    
    def imprimir_LeitosNeonatais(self):
        return self.LeitosNeonatais
    
# *******************************************************

    def inserir_leito(self, valor): 

        

        if valor.tipo_leito() == "Adulto":
            self.LeitosAdultos.queue(valor)       # 1 = Adulto, 2 = Pediátrico, 3 = Neonatal
            return True
        
        elif valor.tipo_leito() == "Pediátrico":
            self.LeitosPediátricos.queue(valor)
            return True
        else:
            self.LeitosNeonatais.queue(valor)
            return True
 
        
    
    def inserir_Ordenado(self, lista, valor):

        lista_atual = lista
        tamanho = lista.tamanho()

        if valor.precisaUTI():

            # Caso a fila esteja vazia, insere diretamente
            if tamanho == 0:
                lista_atual.queue(valor)
                return True

            # Converte o estado do novo paciente para seu nível de prioridade
            novo_estado = valor.estado_paranumero()

            # Cria uma nova fila
            nova_fila = [None] * (tamanho + 1)

            inserido = False
            j = 0  #índice para nova fila

            # Andando na fila original
            for i in range(tamanho):
                paciente_atual = lista_atual.dequeue()
                estado_atual = paciente_atual.estado_paranumero()

                # Insere o novo paciente se ainda não foi inserido e sua prioridade é maior
                if not inserido and novo_estado > estado_atual:
                    nova_fila[j] = valor
                    j += 1
                    inserido = True

                
                nova_fila[j] = paciente_atual # Insere o paciente atual na nova fila
                j += 1

            if not inserido:
                nova_fila[j] = valor

            for k in range(tamanho + 1):
                lista_atual.queue(nova_fila[k])

            return True


    def vincular_Paciente(self, valor):

        vaga = valor.defineVaga()  # Determina o tipo de leito necessário
        fila_atual = None

        if vaga == "Adulto":
            fila_atual = self.LeitosAdultos

        elif vaga == "Pediátrico":
            fila_atual = self.LeitosPediátricos

        elif vaga == "Neonatal":
            fila_atual = self.LeitosNeonatais

        if not fila_atual.empty() and valor.precisaUTI():
            leito = fila_atual.verificar_primeiro() 

            leito.dar_estado(valor.padronizaEstado())
            leito.dar_paciente(valor.id)

            print(f"Leito vinculado ao paciente {valor.id}: {leito}")
            return fila_atual.dequeue()  # Remove o leito da fila 
        else:
            if not valor.precisaUTI():
        
                print(f"Paciente: {valor.id} (vaga:{vaga} estado:{valor.padronizaEstado()}) não necessita de internação.")
                # Adiciona o paciente à fila de espera se não houver vagas disponíveis
                return fila_atual.dequeue()
            
            print(f"Paciente: {valor.id} (vaga:{vaga} estado:{valor.padronizaEstado()}) adicionado à fila de espera.")
            return self.inserir_Ordenado(self.Fila_de_Espera, valor) 
        
    def vincular_Espera(self):

        if self.Fila_de_Espera.empty():
            return False
          
        return self.vincular_Paciente(self.Fila_de_Espera.dequeue())


    def liberar_leito(self, tipo_leito, id_leito):
   
        fila_atual = None

        #Identificando o tipo do leito
        if tipo_leito == "Adulto":
            fila_atual = self.LeitosAdultos

        elif tipo_leito == "Pediátrico":
            fila_atual = self.LeitosPediátricos

        elif tipo_leito == "Neonatal":
            fila_atual = self.LeitosNeonatais

        nova_fila = c.cFila()
        leito_encontrado = False

        # Percorre a fila atual e procura pelo leito com o ID especificado
        while not fila_atual.empty():

            leito = fila_atual.dequeue()

            if leito.id == id_leito:

                leito_encontrado = True

            else:
                nova_fila.queue(leito)

        # Atualiza a fila original com os leitos restantes
        while not nova_fila.empty():
            fila_atual.queue(nova_fila.dequeue())

    
        return  f"Leito {id_leito} do tipo {tipo_leito} liberado com sucesso."
    
   
# *******************************************************
# ***                                                 ***
# *******************************************************

if __name__ == '__main__':

    fila= c.cFila()

    C_Leitos= Gerenciador_Leitos()
    leitos=[C_Leitos.inserir_leito(cl.cLeito()) for x in range(5)]

    print("Leitos Disponiveis:")
    print(C_Leitos)

    

    


    





    


    



