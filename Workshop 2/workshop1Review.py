# this imports the random class from the Python library
import random

# empty parentheses implies this method takes no parameters
# always intent when writing the contents of a method!
def helloworld_void():
    # print(string_parameter) outputs string_parameter
    print("Hello world")
    # the absense of the return method implies the method
    # simply exits

def helloworld():
    return "Hello world"

# takes two parameters num1, num2
def is_num_greater(num1,num2):
    if (num1 > num2): # if (True):
        return True
    elif (num1 == num2):
        return False
    elif (num1 < num2):
        return False

def is_num_greater_zen(num1, num2):
    return num1 > num2

def compare_zen(num1,num2):
    # initializing variables;
    # name goes on the left and value on the right
    non_zen = is_num_greater(num1,num2)
    print("Calling is_num_greater("+str(num1)+","+str(num2)+") returns: ")
    print(non_zen)
    print("Calling is_num_greater_zen("+str(num1)+","+str(num2)+") returns: ")
    print(is_num_greater_zen(num1,num2))
    
def main():
    helloworld_void()
    # since calling helloworld() returns a string,
    # we have to manually print() it
    print(helloworld())
    # str(parameter) turns parameter to printable strings.
    # the use of commas (,) turns multiple string parameters
    # into a tuple, a static list. Parameters will be
    # seperated by spaces
    print("A random value:",str(random.randint(1,100)))
    compare_zen(3,3)
    compare_zen(4,3)
    
main()


    
    
    
