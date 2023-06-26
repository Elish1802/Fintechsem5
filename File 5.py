class Cars:
    id = 101
    name = 'XUV'
    def display(self):
        print("Id:%d\nName:%s"%(self.id,self.name))
car = Cars()
car.display()