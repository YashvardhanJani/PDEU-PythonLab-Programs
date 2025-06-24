# 13. Convert bytes into KB, MB and GB.

def byteToKB_MB_GB():
    a = float(input("Enter the value of byte :"))

    b = a/1024
    print(a,"byte =",b,"KB")

    b = a/(1024*1024)
    print(a,"byte =",b,"MB")

    b = a/(1024*1024*1024)
    print(a,"byte =",b,"GB")


byteToKB_MB_GB()    