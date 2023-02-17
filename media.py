class Media:
    Arraynotas=[]
    def notas(self):
        return self.Arraynotas
    
    def add(self, number):
        if number < 0 or number >10:
            raise ValueError
        self.Arraynotas.append(number)
    
    def media(self):
        suma = 0
        for i in self.Arraynotas:
            suma = suma + i
        return suma/len(self.Arraynotas)
