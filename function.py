x = 10
def outer():
    x = 5
    def inner():
        x = 0
        x += 1
        return x
    return inner

f = outer()
print(f())
print(f())