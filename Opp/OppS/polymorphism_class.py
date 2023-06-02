class Bangladesh():
    def capital(self):
        print("Dhaka is the capital of Bangladesh.")

    def language(self):
        print("Bangla is the primary language of Bangladesh.")

    def type(self):
        print("Bangladesh is a little country.")

class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the primary language of India.")

    def type(self):
        print("India is a big country.")

# main function
bangladesh = Bangladesh()
india = India()
for country in (bangladesh, india):
    country.capital()
    country.language()
    country.type()
    