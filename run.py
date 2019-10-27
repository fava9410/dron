from dron import Dron
import concurrent.futures
import re
import threading

output = '({},{}) dirección {}\n'

def orders(file_content, dr):
    log_orders = ''
    regex = '^[AID]+$'
    for line in file_content:
        if re.search(regex, line) == None:
            return 2, log_orders + "El archivo contiene comandos invalidos"
        for command in line:
            if dr.identify_command(command) == 1: #El dron salio del alcance
                return 1, log_orders + "No fue posible entregar debido a que el dron esta fuera de alcance"
        log_orders += output.format(dr.posX, dr.posY, dr.orientation)
    return 0, log_orders

def delivery(name):
    dr = Dron(6, 3) #cuadras a la redonda + 1 y carga maxima

    try:
        with open('in11.txt') as f:
            number_of_lines = sum(1 for _ in f)

        if number_of_lines <= dr.maxDeliveries:
            file_in = open('in.txt', 'r')
            try:
                file_out = open('files/out{}.txt'.format(name), 'w')

                error, result = orders(file_in, dr)
                if  error == 1:
                    print("El dron esta fuera de alcance, se extravio en: {},{} sentido {} ".format(dr.posX, dr.posY, dr.orientation))

                file_out.write(result)
                file_in.close()
                file_out.close()
            except Exception as e:
                print('Error ',str(e))
        else:
            print('Demasiados domicilios!!!!')
    except:
        print("No se encontro el archivo de entrada #{}".format(name))


delivery(1)
#with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    #executor.map(delivery, range(20))
