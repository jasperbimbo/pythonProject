class Human:

    leg_count=4
    can_walk=True

    def get_description(self):
        return "this is human"

    def get_leg_count(self, count):
         self.leg_count = count

Leg = Human()


print(Leg.get_description())

print(Leg.leg_count)