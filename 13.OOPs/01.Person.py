class Person:
    # Class attributes
    species = "Homo Sapiens"

    def __init__(self, n, a):
        # instance attributes
        self.name = n
        self.age = a

    def __str__(self):
	# will print this below f-string when we print object using print statement
        return f"Species : {self.species}, Name : {self.name}, Age : {self.age}"

    def modify(self, n, a):
        """Can modify using modify method""" #docstring __doc__
        self.name = n
        self.age = a

    def can_vote(self):
        if self.age > 17 :
            print("Eligible to vote")
        else :
            print("Not Eligible to vote")


def main():
    p1 = Person("Gagan Rathia", 17)
    print(p1)
    p1.can_vote()
    print(p1.modify.__doc__)
    p1.modify("Ganpati Rathia",33)
    print(p1)
    p1.can_vote()
    p1.species = "Naja Naja"
    p2 = Person("Ganga Ram",23)
    print(p2)
    print(p1)

if __name__ == "__main__":
    main()
