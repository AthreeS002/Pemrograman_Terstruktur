import random

def randomString(string, n):

    listString = list()

    while True:

        acakString = ''.join(random.sample(string, len(string)))

        if acakString not in listString:
            listString.append(acakString)
        if (len(listString) == n):
            break

    print(listString)

randomString('aku', 1)
randomString('aku', 2)
randomString('aku', 3)
randomString('aku', 4)
