import json

def cargar_inventario():
    try:
        with open('inventario.json', 'r') as file:
            inventario = json.load(file)
    except FileNotFoundError:
        inventario = []
    
    return inventario

def guardar_inventario(inventario):
    with open('inventario.json', 'w') as file:
        json.dump(inventario, file, indent=4)

def crear_producto():
    inventario = cargar_inventario()
    
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad en stock: "))
    
    for producto in inventario:
        if producto['nombre'] == nombre:
            print("¡Error! Ya existe un producto con ese nombre.")
            return
    
    nuevo_producto = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    
    inventario.append(nuevo_producto)
    guardar_inventario(inventario)
    print("Producto creado exitosamente.")

def mostrar_productos():
    inventario = cargar_inventario()
    
    if not inventario:
        print("No hay productos en el inventario.")
    else:
        print("Productos en el inventario:")
        for producto in inventario:
            print(f"Nombre: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

def mostrar_informacion_producto():
    inventario = cargar_inventario()
    
    nombre = input("Ingrese el nombre del producto: ")
    
    for producto in inventario:
        if producto['nombre'] == nombre:
            print(f"Información del producto '{nombre}':")
            print(f"Precio: {producto['precio']}")
            print(f"Cantidad en stock: {producto['cantidad']}")
            return
    
    print("No se encontró un producto con ese nombre.")

def actualizar_producto():
    inventario = cargar_inventario()
    
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    
    for producto in inventario:
        if producto['nombre'] == nombre:
            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
            nueva_cantidad = int(input("Ingrese la nueva cantidad en stock: "))
            
            producto['precio'] = nuevo_precio
            producto['cantidad'] = nueva_cantidad
            
            guardar_inventario(inventario)
            print("Producto actualizado exitosamente.")
            return
    
    print("No se encontró un producto con ese nombre.")

def eliminar_producto():
    inventario = cargar_inventario()
    
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    
    for producto in inventario:
        if producto['nombre'] == nombre:
            inventario.remove(producto)
            guardar_inventario(inventario)
            print("Producto eliminado exitosamente.")
            return
    
    print("No se encontró un producto con ese nombre.")

while True:
    print("--- Gestión de Inventario ---")
    print("1. Crear producto")
    print("2. Mostrar todos los productos")
    print("3. Mostrar información de un producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        crear_producto()
    elif opcion == '2':
        mostrar_productos()
    elif opcion == '3':
        mostrar_informacion_producto()
    elif opcion == '4':
        actualizar_producto()
    elif opcion == '5':
        eliminar_producto()
    elif opcion == '6':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")