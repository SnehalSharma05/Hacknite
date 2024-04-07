import json
import os
import re
from classes import user, Gryffindor, Ravenclaw, Hufflepuff, Slytherin


def typeCheck(data):
    '''
    Checks if the data being passed is of the correct type.

    Param: data - [(obj, type), (obj, type)]
    data should be in the form of list of tuples, the first element of tuple is the object that needs
    to be checked and the second element is the type which it should be.
    '''

    for x in data:
        if not isinstance(x[0], x[1]):
            print(f"Invalid type: {x}")
            raise TypeError


def getDumpUser(lst):
    '''
    Readies the dump for dumping into the json file.

    Param: lst - [user1, user2, ...]
    '''
    typeCheck([(lst, list)])

    dic = []

    for x in lst:
        l = vars(x)
        l['house'] = str(l['house'])
        dic.append(l)

    return dic


def getDumpHouse(lst):
    '''
    Readies the dump for dumping into the json file.

    Param: lst - [house1, house2, ...]
    '''
    typeCheck([(lst, list)])

    dic = []

    for x in lst:
        l = vars(x)
        if 'students' in l:
            del l['students']
        if 'role' in l:
            del l['role']
        dic.append(l)

    return dic


def clearTag(response, tag=1220419669379383376):
    '''
    Removes the tag of the response that occurs in the start.
    '''
    return re.sub(f"<@{tag}> ", "", response)


def readAmajeDataUser(data):
    '''
    Reads the data from the json file.
    And then makes the user objects.
    '''

    if (data == {}):
        return

    for x in data['users']:
        u = user(x["name"], x["id"], x["house"], x["wand"], x["points"], x["wealth"],
                 x["potions"], x["spells"], x["items"], x["progress"], x["enemiesDefeated"])

        house = eval(x["house"])

        if (house):
            house.students.append(u)

            if house.name == "Gryffindor":
                Gryffindor.students.append(u)
            elif house.name == "Ravenclaw":
                Ravenclaw.students.append(u)
            elif house.name == "Hufflepuff":
                Hufflepuff.students.append(u)
            elif house.name == "Slytherin":
                Slytherin.students.append(u)


def readAmajeDataHouse(data):
    '''
    Reads the data from the json file.
    And then makes the house objects.
    '''

    if (data == {}):
        return

    for x in data['house']:
        eval(f"{x['name']}").points = x['points']


class dataHandler:
    def __init__(self, fileName='user_data.json'):
        self.__createFile(fileName)
        self.__pathToFile = f'assets/{fileName}'

    def __createFile(self, fileName: str) -> None:
        '''
        Checks and gets the file handle for the file that we are using.
        '''

        typeCheck([(fileName, str)])

        if 'assets' not in os.listdir('.'):
            os.mkdir('assets')
            fh = open('assets/' + fileName, 'w')
            fh.close()

        elif fileName not in os.listdir('./assets'):
            fh = open('assets/' + fileName, 'w+')
            fh.close()

    def dump(self, data: list, func=lambda x: [], key='heh') -> None:
        '''
        Here data is an iterable of dictionaries that contain properties of data (dictionaries) to dump.
        Note: The entire file is wiped clean, and then new data written on it.
        '''

        data = func(data)

        typeCheck([(data, list)])
        for x in data:
            typeCheck([(x, dict)])

        json_data = json.dumps({f'{key}': data}, indent=4)
        with open(self.__pathToFile, 'w') as fh:
            fh.write(json_data)

    def read(self, func=lambda x: True) -> None:
        '''
        We read and return the data in the same way it was dumped (form of a).
        '''

        try:
            with open(self.__pathToFile, 'r') as fh:
                data = json.load(fh)

        except:
            data = {}

        func(data)


if __name__ == '__main__':
    obj = dataHandler()
    obj.dump([{'name': 'Gathik Jindal', 'track': 'Discord bot'},
              {'name': 'Snehal Sharma', 'track': 'Discord bot'},
              {'name': 'Vriddhi Agarwal', 'track': 'Discord bot'}])

    l = obj.read()
    print(l)
