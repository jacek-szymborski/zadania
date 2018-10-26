def test_check_range():
    assert check_range(1,0,5) == True

def check_range(liczba,zmin,zmax):
    if liczba >= zmin and liczba <= zmax:
        return True


print(check_range(1,0,3))