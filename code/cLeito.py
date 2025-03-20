import random as rd

# A classe abaixo é o leito(código, disponível, tipo(Faixa Etária), Paciente(código))

class cLeito:

    def __init__(self, Paciente = None):
        
        self._codigo     = rd.randint(1,20)
        self.estado = None
        self._Paciente   = Paciente
        tipos= ["Adulto","Pediátrico","Neonatal"]
        self.tipo= rd.choice(tipos)    # Adulto, Pediátrico, Neonatal
       
        
    def __str__(self):

        strleito= f" | LeitoID:{self._codigo} | Paciente: {self._Paciente} | Situação: {self.estado} | Tipo: {self.tipo} |"
        return strleito

##############################################################

    def gerador_leitos():
        tipos= ["Adulto","Pediátrico","Neonatal"]
        pass
    
##############################################################

    def codigo(self):
        self._codigo= rd.randint(1,200) # Precisa modificar a forma como vou gerar o código do Leito
        return self._codigo

    def tipo_leito(self):
        return self.tipo
    
    def dar_tipo_leito(self, faixa): #APAGAR
        self.tipo= faixa
        return True
    
    def dar_paciente(self,nome):
        self._Paciente = nome 
        return True
    
    def dar_estado(self,v):
        self.estado= v
        return True

if __name__ == '__main__':

    leitos=[cLeito() for x in range(5)]

    print("Leitos:")
    for i in range(5):
        print(leitos[i])