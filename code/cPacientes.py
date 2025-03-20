import random

class Paciente:
    def __init__(self): #A idade será dada em meses

        estados = ["vermelho", "laranja", "amarelo", "verde", "azul"]

        self.id = random.randint(1, 100)
        self.idade = random.randint(0, 1200) # 1200 equivale a 100 anos de idade em meses
        self.estado = random.choice(estados)
   

    def precisaUTI(self):

        if self.estado == "vermelho" or self.estado == "laranja" or self.estado == "amarelo":
            return True

        else:
            return False
    
    #Aqui estamos tratando a idade em meses para abrangir o Neonatal
    def defineVaga(self):
        if 0 <= self.idade < 11: 
            return "Neonatal"
        
        if 12 <= self.idade <= 156: 
            return "Pediátrico"

        if  self.idade > 156: 
            return "Adulto"

    def idadeEmAnos(self):

        anos = self.idade // 12  
        if anos == 0:  # Se a idade for menos de 1 ano
            return f"{self.idade} meses"

        return f"{anos} anos"

    def padronizaEstado(self):

        if self.estado == "vermelho":
            estado = "Emergência"

        elif self.estado == "laranja":
            estado = "Muito urgente"

        elif self.estado == "amarelo":
            estado = "Urgente"

        elif self.estado == "verde":
            estado = "Pouco urgente"

        elif self.estado == "azul":
            estado = "Não urgente"

        else:
            estado = "Estado não existente"

        return estado

    def __str__(self):

        idadeOut = self.idadeEmAnos()
        estado = self.padronizaEstado()

        strg = f"Paciente: {self.id}, Idade: {idadeOut}, Estado: {estado}"

        return strg
    
    def estado_paranumero(self):
        valor= self
        estado=None
        if valor.estado == "vermelho":
                estado = 5
        elif valor.estado == "laranja":
            estado = 4
        elif valor.estado == "amarelo":
            estado = 3
        elif valor.estado == "verde":
            estado = 2
        elif valor.estado == "azul":
            estado = 1
        return estado

if __name__ == '__main__':

    pacientes = [Paciente() for i in range(5)] # Abstração de um for que adiciona 5 pacientes em uma lista, list compresion
    for paciente in pacientes:
        print(paciente)
