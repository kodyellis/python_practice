employee={'Alex':1500, 'jogf':1342, 'larr':1200 }
def test(employee):
    new={'Buck':2000, 'stan':4000}
    employee.update(new)
    print("the function inside:", employee)
    return
test(employee)
print("outside",employee)
