class Human:

    leg_count = 4
    gender = "female"

    def get_gender(self):
        return "unknown"

class Man(Human):
    gender = "male"

    def get_gender(self):
        return self.gender

class Woman(Human):
      gender = "woman"

      def get_gender(self):
          return self.gender

human = Human()

print("Human:", human.get_gender())

man = Man()
print("Man:", man.get_gender())

woman = Woman()
print("Woman:", woman.get_gender())


