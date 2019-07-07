"""
1) Create two variables – one with your name and one with your age
2) Create a function which prints your data as one string
3) Create a function which prints ANY data (two arguments) as one string
4) Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)"""

def get_name():
    return input("Enter your name: ")


def get_age():
    return input("Enter your age: ")

name = get_name()
age = get_age()

def print_info():
    global name
    global age
    print(name + " " + age)

def print_any():
    int = 5
    print("Hello " + str(int))



def age_decade_calc():
    global age
    decade = (int(age))/10
    print(int(decade))

print_info()
print_any()
age_decade_calc()