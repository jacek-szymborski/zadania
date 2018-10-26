def test_sumator():
    assert sumator((8, 2, 3, 0, 7)) == 20
    assert sumator((0, 0, 0, 0)) == 0

def sumator(lista):
    suma = sum(lista)

    return suma

print(sumator((8, 2, 3, 0, 7)))