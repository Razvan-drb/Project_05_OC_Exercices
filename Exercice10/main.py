## Écrivez votre code ici !
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def afficher_details(self):
        print(f"Nom: {self.name}, Âge: {self.age}")


class Employee(Person):
    def __init__(self, name, age, salaire):
        super().__init__(name, age)
        self.salaire = salaire

    def afficher_details(self):
        super().afficher_details()  # appel de la méthode de la classe mère
        print(f"Salaire: {self.salaire}")


personne = Person("Alice", 30)
employe = Employee("Bob", 40, 50000)

personne.afficher_details()
employe.afficher_details()
