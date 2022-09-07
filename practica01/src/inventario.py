"""
La biblioteca pandas es usada en este programa para la manipulacion de los datos.
"""
import pandas as pd

def menu():
    """
    Nos permite tener un menu interactivo con el usuario. El usuario puede 
    seleccionar las opciones de interacción con el programa desde una terminal.
    El programa termina cuando el usuario selecciona la opción de terminar con 
    la ejecución del sistema.
    """
    opcion=""
    while opcion!="z":
        print("\n\nSistema de inventario para farmacias:\n\n"
                +"Selecciona una opcion:\n"
                +"[a] Ver todo el inventario actual.\n"
                +"[b] Agregar medicamento.\n"
                +"[c] Eliminar medicamento.\n"
                +"[d] Seleccionar por ID.\n"
                +"[e] Seleccionar por Nombre.\n"
                +"[f] Seleccionar por Categoria.\n"
                +"[g] Editar registro.\n"
                +"[h] Hacer una compra.\n"
                +"[z] Salir del sistema.")

        opcion=str(input())

        match opcion:
            case "a":
                inventory_data=reload()
                print("\nInventario actual:\n")
                print(inventory_data)

            case "b":
                add_med()

            case "c":
                del_med()

            case "d":
                select_id()

            case "e":
                select_name()

            case "f":
                select_category()

            case "g":
                modify_row()

            case "h":
                buy()

            case "z":
                print("\n\nSaliendo del sistema...")
                break

            case _:
                print("\nOpcion invalida")

def reload():
    """
    Función auxiliar que nos permite obtener un DataFrame de la información contenida
    en el csv. Se selecciona a la columna "ID" como identificador por defecto de 
    los registros. Se usan los métodos "read_csv" y "set_index" de la bibliotaca
    "pandas".
    """
    inventory_data=pd.read_csv('files/inventario/inventario.csv')
    inventory_data.set_index('ID', inplace=True)
    return inventory_data

def add_med():
    """
    Nos permite agregar un nuevo medicamento a los registros. Todos los datos
    del nuevo medicamento deben de ser ingresados desde la terminal, incluído el
    identificador (el cual debe ser numérico, de no ser así se lanzará una
    excepción). No se permiten añadir nuevos registros con identificador repetido.
    """
    ids=pd.read_csv('files/inventario/inventario.csv')
    ids=ids['ID'].tolist()
    print("\nAgregar medicamento:\n"
            +"Nombre del medicamento a agregar: ")
    nombre=str(input())
    print("\nCategoria del medicamento:")
    categoria=str(input())
    while True:
        try:
            print("\nPrecio:")
            precio=int(input())
            break
        except:
            print("\nDatos invalidos. Intentese otra vez")
    
    while True:
        try:
            print("\nCantidad:")
            cantidad=int(input())
            break
        except:
            print("\nDatos invalidos. Intentese otra vez")

    while True:
        try:
            print("\nIdentificador:")
            identificador=int(input())
            if(identificador in ids):
                while (identificador in ids):
                    print("\nIdentificador repetido, por favor ingrese uno distinto")
                    identificador=int(input())
            break
        except:
            print("\nDatos invalidos. Intentese otra vez")

    new_med={
        'ID': identificador,
        'Nombre': nombre,
        'Categoria': categoria,
        'Precio': [precio],
        'Cantidad en existencia': [cantidad]
    }

    df=pd.DataFrame(new_med)
    df.to_csv('files/inventario/inventario.csv', mode='a', index=False, header=False)
    print("\nOperacion realizada con exito")

def del_med():
    """
    Nos permite eliminar el registro de un medicamento. El medicamento a eliminar
    es buscado por su identificador. En caso de recibir un identificador que no
    corresponde a ningún registro, se lanza una excepción.
    """
    print("\nEliminar un medicamento\n")
    
    while True:
        try:
            print("\nIngresa el identificadoe del elemento a eliminar")
            identificador=int(input())
            break
        except:
            print("\nDatos invalidos. Intentese otra vez")


    try:
        delete_data=reload()
        delete_data=delete_data.drop(identificador)
        delete_data.to_csv('files/inventario/inventario.csv')
    except KeyError:
        print("\nNo se encontro ningun registro con ese identificador")

    print("\nOperacion realizada con exito")

def select_id():
    """
    Nos permite acceder a un registro en específico buscándolo por su identificador.
    Al no haber identificadores reopetidos, solo regresará un único registro a la vez.
    """
    while True:
        try:
            print("\nIngrese el identificador del elemento a buscar:")
            identificador=int(input())
            break
        except:
            print("\nDatos invalidos. Intentese otra vez")

    data_id=reload()
    busqueda='ID=='+str(identificador)
    df=data_id.query(busqueda) 
    print(df)



def select_category():
    """
    Nos permite acceder a todos los registros que tengan una categoria en específico.
    Si no se encuentra la categoria se regresa un registro vacío.
    """
    print("\nIngresa la categoria")
    categoria=str(input())
    data_category=reload()
    data_category=data_category[data_category['Categoria'].str.contains(categoria)]
    print(data_category)


def select_name():
    """
    Nos permite acceder a un registro en específico buscándolo por su nombre. Puede
    haber varios registros con el mismo nombre, por ejemplo un mismo medicamento
    de distinta marca. Si no se encuentra el nombre se regresa un registro vacío.
    """
    print("\nIngresa la categoria")
    categoria=str(input())
    data_name=reload()
    data_name=data_name[data_name['Categoria'].str.contains(categoria)]
    print(data_name)
    
def modify_row():
    """
    Funcion que nos permite modificar un registro de nuestro archivo csv.
    Los valores que se pueden modificar son los siguientes: Nombre, Categoria,
    Precio y Cantidad de existencia. El registro a ser modificado se busca 
    mediante su identificador, en caso de que el usuario ingrese un identificador
    que no está asociado a ningún registro se regresa al menú principal.
    """
    print("\nModificar medicamento")
    while True:
        try:
            print("\nIngresa el identificadoe del elemento a modificar")
            identificador=int(input())
            break
        except:
            print("\nDatos invalidos. Intentese otra vez")
    ids=pd.read_csv('files/inventario/inventario.csv')
    ids=ids['ID'].tolist()
    data=reload()

    if(not (identificador in ids)):
        print("No se tiene registro con dicho modificador")
        return

    print("\nQue deseas modificar:\n"
            +"[a] Nombre\n"
            +"[b] Categoria\n"
            +"[c] Precio\n"
            +"[d] Cantidad en existencia")
    seleccion=str(input())

    match seleccion:
        case "a":
            print("\nIngresa el nuevo nombre:")
            nombre=str(input())
            data.loc[identificador, 'Nombre']=nombre
            data.to_csv('files/inventario/inventario.csv')
            print("\nOperacion realizada con exito")

        case "b":
            print("\nIngresa la nueva categoria:")
            cat=str(input())
            data.loc[identificador, 'Categoria']=cat
            data.to_csv('files/inventario/inventario.csv')
            print("\nOperacion realizada con exito")
            
        case "c":
            while True:
                try:
                    print("\nIngresa el nuevo precio:")
                    precio=int(input())
                    break
                except:
                    print("\nDatos invalidos. Intentese otra vez")

            data.loc[identificador, 'Precio']=precio
            data.to_csv('files/inventario/inventario.csv')
            print("\nOperacion realizada con exito")

        case "d":
            while True:
                try:
                    print("\nIngresa la nueva cantidad de existencia:")
                    cantidad=int(input())
                    break
                except:
                    print("\nDatos invalidos. Intentese otra vez")

            data.loc[identificador, 'Cantidad en existencia']=cantidad
            data.to_csv('files/inventario/inventario.csv')
            print("\nOperacion realizada con exito")

        case _:
            print("\nOpcion invalida")

def buy():
    print("En desarrollo.")


"""
Main del programa. Se invoca la función "menu", que permite la interaccion con
el programa.
"""
menu()
