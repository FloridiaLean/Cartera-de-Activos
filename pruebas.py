from calculos import *
from menu import *
from operaciones import *
from persistencia  import *
from posiciones import *
from servicios import *
from utilidades import *
from validaciones import *
from visualizacion import *

operaciones = cargar_operaciones()
posiciones = cargar_posiciones()


menu_principal(operaciones,posiciones)



