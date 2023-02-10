with open("data.txt", "r") as archivo:
    
    for linea in archivo.readlines():
        tokens=linea.split(" ")
        print(tokens)

