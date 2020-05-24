# Permanently saving data

import pickle


class Person():

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        print('You have crated a new person named: ', self.name)

    def __str__(self):
        # Formating the message
        return '{} {} {}'.format(self.name, self.gender, self.age)


class PeopleList():

    people = []

    def __init__(self):

        peopleListF = open('PeopleList', 'ab+')  # ab+ adding binary inf
        peopleListF.seek(0)

        try:
            self.people = pickle.load(peopleListF)
            print('{} people loaded from the external file'.format(len(self.people)))
        except:
            print('Empty file')
        finally:
            peopleListF.close()
            del(peopleListF)

    def addPers(self, p):
        self.people.append(p)
        self.saveData()

    def showList(self):
        for p in self.people:
            print(p)

    def saveData(self):
        peopleListF = open('PeopleList', 'wb')
        pickle.dump(self.people, peopleListF)
        peopleListF.close()
        del(peopleListF)

    def retrData(self):
        print('Data on file: ')
        for p in self.people:
            print(p)


peopleList = PeopleList()
person1 = Person('Gio', 'Male', '26')
peopleList.addPers(person1)
person2 = Person('Andres', 'Male', '26')
peopleList.addPers(person2)
peopleList.retrData()
