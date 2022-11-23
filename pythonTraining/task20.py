class Human:

    leg_count = 4
    gender = "female"

    def get_gender(self):
        return "unknown"

class Man(Human):
      gender = "male"

human = Human()
print(human.get_gender())

man = Man()
print(man.gender)