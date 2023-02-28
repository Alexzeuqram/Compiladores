with open('data.txt', 'r') as file:  #Con With creamos la instancia y una vez terminado destruye la instancia.
#file = open('data.txt', 'r')
    for linea in file.readlines():
        tokens = linea.split(' ')
        print(tokens)

#file.close()