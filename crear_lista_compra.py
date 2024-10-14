# Creamos la  estructura de datos adecuado para ingresarlo a la función como parámetro
menu = {
    'Aperitivo': {'nombre': 'Guacamole',

           'ingredientes': ['cilantro', 'cebolla','chile', 'ajo','tomate','aguacates','limón','sal']
        },

    'Primer plato':{
        'nombre': 'Pimientos del piquillo rellenos',
        'ingredientes': ['huevo','palitos de cangrejo','atún en aceite de oliva', 'pimientos del piquillo','pimiento verde', 'pimiento rojo','cebolla', 'vinagre de vino', 'sal',  'aceite de oliva virgen extra']

    },

    'segundo plato': {
        'nombre': 'Solomillo de cerdo agridulce',
        'ingredientes': ['aceite de oliva','ajo', 'solomillo de cerdo', 'cebolla' , 'manzana', 'tomate','calabacines','brandy','vino de oporto','ciruelas pasas', 'albricoque', 'mostaza','piñones',]

    },

    'Postre' : {
        'nombre': 'Brownie de chocolate con helado de turron',
        'ingredientes':['chocolate amrgo', 'cacao', 'mantequilla','azucar' ,'huevos', 'sal', 'harina de trigo', 'nueces']
    }

}

# Definimos la función 

def crea_lista_compra(menu):

    # validaciones
    if not  isinstance(menu, dict):
        return f'Error: {menu} no es una estructura válida, no es un diccionario'

    # inicializa variable de resultado
    lista_compra = []

    for plato in menu:  # recorre los platos del menu incluyendo el aperitivo y el postre
        for ingrediente in menu[plato]['ingredientes']: # recorre los ingredientes de cada plato
            if ingrediente not in lista_compra: # verifica que no haya ingrediente repetido
                lista_compra.append(ingrediente)  # Agrega ingrediente  a la lista vacia

    return lista_compra

# imprime la lista de compra en consola
print('Lista de compra:')

for ingrediente in  crea_lista_compra(menu):
    print(f'-{ingrediente}')