# function is a first class object
def double_decker():
    print("I am the outer function")
    def inner_func():
        print("I am the inner function")
        return "I am the return value of inner function"
    return inner_func()
    
print(double_decker())

def do_something(work):
    print('work is done')
    # print(work)
    work()
    print('work endend')
# do_something('ami busy')

def codin():
    print('I am coding')

do_something(codin)