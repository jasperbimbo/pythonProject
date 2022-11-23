class Human:

     name = 'Bimbo'
     age = 24

     def get_name_age(self):
        return self.name + ',' + str(self.age)

human = Human()
print(human.get_name_age())