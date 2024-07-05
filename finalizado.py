import os

def cargar_inventario(nom_archivo):
    invent = {}
    try:
        if os.path.exists(nom_archivo):
            with open(nom_archivo, 'r') as f:
                for linea in f:
                    if linea.strip():  
                        nombre, precio, cantidad = linea.strip().split(',')
                        invent[nombre] = {'precio': float(precio), 'cantidad': int(cantidad)}
    except IOError as e:
        print(f"Error en el archivo: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return invent


def guardar_inventario(invent, nom_archivo):
    try:
        with open(nom_archivo, 'w') as f:
            for producto, detalles in invent.items():
                f.write(f"{producto},{detalles['precio']},{detalles['cantidad']}\n")
        print("Inventario guardado con éxito.")
    except IOError as e:
        print(f"Error en el guardado del archivo: {e}")
    except Exception as e:
        print(f"Ha surgido un error inesperado: {e}")


def registrar_producto(invent):
    try:
        nombre = input("Ingrese nombre del producto: ")
        precio = float(input("Ingrese precio del producto: "))
        cantidad = int(input("Ingrese cantidad del producto: "))
        invent[nombre] = {'precio': precio, 'cantidad': cantidad}
        print(f"Producto '{nombre}' registrado con éxito!")
    except ValueError:
        print("Error: Ingrese un número válido para precio o cantidad.")
    except Exception as e:
        print(f"Ha surgido un error inesperado: {e}")


def actualizar_inventario(invent):
    try:
        nombre = input("Ingrese el nombre del producto que desee actualizar: ")
        if nombre in invent:
            nueva_cantidad = int(input(f"Ingrese una nueva cantidad para '{nombre}': "))
            invent[nombre]['cantidad'] = nueva_cantidad
            print(f"Inventario de '{nombre}' actualizado!")
        else:
            print(f"El producto '{nombre}' no se ha encontrado en el inventario.")
    except ValueError:
        print("Error: Debe ingresar un número válido para la nueva cantidad de producto.")
    except Exception as e:
        print(f"Ha surgido un error inesperado: {e}")


def mostrar_inventario(invent):
    try:
        print("Inventario actual:")
        print("Nombre\t\tPrecio\t\tCantidad")
        for producto, detalles in invent.items():
            print(f"{producto}\t\t{detalles['precio']}\t\t{detalles['cantidad']}")
    except Exception as e:
        print(f"Error al mostrar el inventario: {e}")


def principal():
    nom_archivo = 'inventario.txt'
    invent = cargar_inventario(nom_archivo)

    while True:
        try:
            print("\nMenú:")
            print("1. Registrar producto")
            print("2. Actualizar inventario")
            print("3. Mostrar inventario")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                registrar_producto(invent)
            elif opcion == '2':
                actualizar_inventario(invent)
            elif opcion == '3':
                mostrar_inventario(invent)
            elif opcion == '4':
                guardar_inventario(invent, nom_archivo)
                print("### INVENTARIO FINALIZADO ###")
                break
            else:
                print("Opción invalida... ingrese una nueva opción.")
        except Exception as e:
            print(f"Error inesperado en el programa principal: {e}")

if __name__ == "__main__":
    principal()
