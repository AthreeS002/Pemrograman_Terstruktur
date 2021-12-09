from datetime import *

def diffDate(x):
    sblm = datetime.date(datetime.now())
    x = datetime.strptime(x, "%Y-%m-%d").date()
    return abs(x-sblm)

print("Selisih harinya adalah: {0}".format(diffDate("2020-12-30").days))
