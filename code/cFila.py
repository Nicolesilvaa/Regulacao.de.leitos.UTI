class cFila:

    def __init__ (self):
            
        self._fila = []
        self._numelements= 0
    

# *******************************************************
# ***                                                 ***
# *******************************************************

    def __str__(self):
        if self._numelements ==0:
            return "VAZIO \n"
        
        strfila= ""
        for i in range(self._numelements):
            strfila+= str(f"{self._fila[i]} -> \n")
        return strfila

# *******************************************************
# ***                                                 ***
# *******************************************************


    def tamanho(self):
        return self._numelements
    
    def empty(self):
        if self._numelements !=0:
            return False
        return True
    
    def queue(self, valor):

        self._fila+=[None]
        self._fila[self._numelements]=valor
        self._numelements+=1
        return True


    def dequeue(self):
        if self._numelements == 0:
            return False
        
    
        valor_removido = self._fila[0]


        for i in range(1, self._numelements):
            self._fila[i - 1] = self._fila[i]
        self._numelements -= 1
        self._fila = self._fila[:self._numelements]

        return valor_removido
    

    def verificar_primeiro(self):
        if self.tamanho() <=0:
            return False
        
        return self._fila[0]
    

if __name__ == '__main__':

    Fila= cFila()
    for i in range(1,20):
        (Fila.queue(i))
        print(Fila)

    print(f" tamanho: {Fila.tamanho()}")
    for i in range(1,20):
        print(Fila.dequeue()) 
        print(f" tamanho: {Fila.tamanho()}")


