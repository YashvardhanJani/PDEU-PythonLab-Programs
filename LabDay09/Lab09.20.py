# 20. Define three functions fun(), disp() and msg(). Store them in a list and call them one by one in a loop.

def fun():
    return "fun() exicuted."

def disp():
    return "disp() exicuted."
    
def msg():
    return "msg() exicuted."   

lst = [fun(), disp(), msg()]        

for l in lst:
    print(l)

# Note: If we write print statment in these three functions then to exicute every fuvtion we should write l in place of print(l).
