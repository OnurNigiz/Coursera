class PartyAnimal:#This is a template for making PartyAnimal objects

#####################################
    x = 0 

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

#Each PartyAnimal object has a bit of data
######################################

an = PartyAnimal()#Construct a PartyAnimal object and store in an variable

an.party()
an.party()
PartyAnimal.party(an)