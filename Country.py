class India():

    def capital(self):
        print("New Delhi is the Capital of India.")

    def lang(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():

    def capital(self):
        print("Washington DC is the Capital of USA.")

    def lang(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):

    country.capital()
    country.lang()
    country.type()