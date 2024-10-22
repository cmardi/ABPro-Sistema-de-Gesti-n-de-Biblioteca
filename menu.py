def menu():
    while True:
        print("\nBienvenidos al Sistema de Gestión de Biblioteca")
        print("Selecciona una de las opciones:")
        print("1. Solicitar préstamo de libros")
        print("2. Devolver libros")
        print("3. Ver lista de libros")
        print("4. Ver lista de préstamos")
        print("5. Agregar un nuevo libro")
        print("6. Eliminar un libro")
        print("7. Agregar un nuevo usuario")
        print("8. Eliminar un usuario")
        print("9. Salir")
        
        opcion = input("Ingresa tu opción: ")
        
        if opcion == '1':
            solicitar_prestamo()
        elif opcion == '2':
            devolver_libro()
        elif opcion == '3':
            ver_lista_libros()
        elif opcion == '4':
            ver_lista_prestamos()
        elif opcion == '5':
            agregar_libro()
        elif opcion == '6':
            eliminar_libro()
        elif opcion == '7':
            agregar_usuario()
        elif opcion == '8':
            eliminar_usuario()
        elif opcion == '9':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
