from dron import Dron
import concurrent.futures
import re
import threading

class Route(object):
    output = '({},{}) dirección {}\n' #formator salida
    regex = '^[AID]+$' #comandos validos
    filename_in = 'in{}.txt'
    filename_out = 'out{}.txt'
    name = ''

    def __init__(self, name):
        self.name = str(name + 1).zfill(2)
        self.filename_in = self.filename_in.format(self.name)
        self.filename_out = self.filename_out.format(self.name)

    def orders(self, file_content, dr):
        log_orders = ''

        for line in file_content:
            if re.search(self.regex, line) == None:
                return 2, log_orders + "La linea contiene comandos invalidos"
            for command in line:
                if dr.identify_command(command) == 1: #El dron salio del alcance
                    return 1, log_orders + "No fue posible entregar debido a que el dron {} \
                    esta fuera de alcance".format(self.name)
            log_orders += self.output.format(dr.posX, dr.posY, dr.orientation)
        return 0, log_orders

    def delivery(self):
        dr = Dron(6, 10) #cuadras a la redonda + 1 y carga maxima

        try:
            with open(self.filename_in) as f:
                number_of_lines = sum(1 for _ in f)

            if number_of_lines <= dr.maxDeliveries:
                with open(self.filename_in) as file_in:
                    try:
                        error, result = self.orders(file_in, dr)
                        if  error == 1:
                            print("El dron {} esta fuera de alcance, se extravio en: \
                            {},{} sentido {} ".format(self.name, dr.posX, dr.posY, dr.orientation))

                        file_out = open('{}'.format(self.filename_out), 'w')
                        file_out.write('== Reporte de entregas ==\n')
                        file_out.write(result)
                        file_out.close()
                    except Exception as e:
                        print('Error ',str(e))
            else:
                print('Demasiados domicilios para dron {}!!!!'.format(self.name))
        except:
            print("No se encontro el archivo de entrada {}".format(self.filename_in))

def create_routes(name):
    route = Route(name)
    route.delivery()

if __name__ == "__main__":
    max_number_drones = 20
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_number_drones) as executor:
        executor.map(create_routes, range(max_number_drones))
