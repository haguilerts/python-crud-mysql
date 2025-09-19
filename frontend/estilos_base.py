from prettytable import PrettyTable
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# ============================
# Funciones de estilo
# ============================

def titulo(texto):
    """
    Muestra un título grande con color.
    """
    print(Fore.CYAN + "\n" + "="*len(texto))
    print(Fore.CYAN + texto)
    print(Fore.CYAN + "="*len(texto))


def exito(texto):
    """
    Mensaje de éxito en verde con símbolo.
    """
    print(Fore.GREEN + "✅ " + texto)


def error(texto):
    """
    Mensaje de error en rojo con símbolo.
    """
    print(Fore.RED + "❌ " + texto)


def aviso(texto):
    """
    Mensaje de aviso o información en amarillo.
    """
    print(Fore.YELLOW + "⚠ " + texto)


def separar_linea():
    """
    Imprime una línea separadora.
    """
    print(Fore.MAGENTA + "-"*50)


def tabla(datos, encabezados):
    """
    Devuelve una tabla PrettyTable lista para imprimir.
    - datos: lista de listas
    - encabezados: lista de nombres de columna
    """
    t = PrettyTable()
    t.field_names = encabezados
    for fila in datos:
        t.add_row(fila)
    return t
