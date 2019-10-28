from dron import Dron
import concurrent.futures
import re
import threading

class Route(object):
    output = '({},{}) dirección {}\n' #formator salida
    regex = '^[AID]+$' #comandos validos
    name = 0
    filename_in = 'in.txt'
    filename_out = 'out.txt'

    def orders(self, file_content, dr):
        log_orders = ''

        for line in file_content:
            if re.search(self.regex, line) == None:
                return 2, log_orders + "La linea contiene comandos invalidos"
            for command in line:
                if dr.identify_command(command) == 1: #El dron salio del alcance
                    return 1, log_orders + "No fue posible entregar debido a que el dron esta fuera de alcance"
            log_orders += self.output.format(dr.posX, dr.posY, dr.orientation)
        return 0, log_orders

    def delivery(self):
        dr = Dron(6, 3) #cuadras a la redonda + 1 y carga maxima

        try:
            with open(self.filename_in) as f:
                number_of_lines = sum(1 for _ in f)

            if number_of_lines <= dr.maxDeliveries:
                with open(self.filename_in) as file_in:
                    try:
                        error, result = self.orders(file_in, dr)
                        if  error == 1:
                            print("El dron esta fuera de alcance, se extravio en: {},{} sentido {} ".format(dr.posX, dr.posY, dr.orientation))

                        file_out = open('{}'.format(self.filename_out), 'w')
                        file_out.write('== Reporte de entregas ==\n')
                        file_out.write(result)
                        file_out.close()
                    except Exception as e:
                        print('Error ',str(e))
            else:
                print('Demasiados domicilios!!!!')
        except:
            print("No se encontro el archivo de entrada {}".format(self.filename_in))

if __name__ == "__main__":
    route = Route()
    route.delivery()
