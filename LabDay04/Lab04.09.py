# 09. Print N natural nos. in reverse

def natural_num_reverse(n):

    for i in range(n,0,-1):
        print(i, end=" ")

n = int(input("Enter the integer number : "))

natural_num_reverse(n)