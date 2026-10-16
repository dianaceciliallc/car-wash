# SISTEMA DE GESTION Y FACTURACION - CARWASH
def mostrar_menu_servicios():
    print("\n\n")
    print("===== CARWASH: SERVICIOS Y TARIFAS =====")
    print('1. Lavado Simple')
    print('2. Lavado de Salon')
    print('3. Encerado')
    print('4. Lavado de Motor')
    print('\nTARIFAS (S/)')
    print('==========================================')
    print("Servicio           Auto   Camioneta   Moto")
    print('==========================================')
    print("1. Lavado simple     15       20        10")
    print("2. Lavado de Salon   25       30        15")
    print("3. Encerado          35       45        25")
    print("4. Lavado de Motor   40       50        30")
    print('==========================================')


def procesar_atenciones(total_recaudado, total_comisiones, contador_servicios):
    cantidad = int(input('
Ingrese la cantidad de vehiculos a registrar en este turno: '))
    while cantidad < 0:
        print('La cantidad no puede ser negativa.')
        cantidad = int(input('Ingrese la cantidad de vehiculos a registrar: '))

    for i in range(cantidad):
        print('
--- Vehículo', i + 1, 'de', cantidad, '---')
        mostrar_menu_servicios()

        servicio = int(input('Seleccione el servicio (1-4): '))
        while servicio < 1 or servicio > 4:
            print('Servicio incorrecto. Intente nuevamente.')
            servicio = int(input('Seleccione el servicio (1-4): '))

        print('
TIPO DE VEHICULO')
        print('1. Auto')
        print('2. Camioneta')
        print('3. Moto')
        tipo = int(input('Seleccione el tipo (1-3): '))
        while tipo < 1 or tipo > 3:
            print('Tipo de vehiculo incorrecto.')
            tipo = int(input('Seleccione el tipo (1-3): '))

        precio = 0
        nombre_servicio = ''

        if servicio == 1:
            nombre_servicio = 'Lavado Simple'
            if tipo == 1:
                precio = 20
            elif tipo == 2:
                precio = 30
            else:
                precio = 10
        elif servicio == 2:
            nombre_servicio = 'Lavado de Salon'
            if tipo == 1:
                precio = 40
            elif tipo == 2:
                precio = 55
            else:
                precio = 20
        elif servicio == 3:
            nombre_servicio = 'Encerado'
            if tipo == 1:
                precio = 35
            elif tipo == 2:
                precio = 50
            else:
                precio = 15
        else:
            nombre_servicio = 'Lavado de Motor'
            if tipo == 1:
                precio = 25
            elif tipo == 2:
                precio = 35
            else:
                precio = 15

        # Porcentaje de comision de ejemplo: 20 % por atencion.
        comision = precio * 0.20
        total_recaudado = total_recaudado + precio
        total_comisiones = total_comisiones + comision
        contador_servicios[nombre_servicio] = contador_servicios[nombre_servicio] + 1

        print('>> Servicio registrado:', nombre_servicio)
        print('>> Precio: S/', format(precio, '.2f'))
        print('>> Comision: S/', format(comision, '.2f'))

    print('
¡Atenciones registradas con éxito!')
    return total_recaudado, total_comisiones, contador_servicios

    
def mostrar_reporte(total_recaudado, total_comisiones, contador_servicios):
    ingreso_neto = total_recaudado - total_comisiones

    print('
========== CIERRE DE CAJA (ACUMULADO) ==========')
    print('Ingresos totales: S/', format(total_recaudado, '.2f'))
    print('Total de comisiones: S/', format(total_comisiones, '.2f'))
    print('Ingreso neto del local: S/', format(ingreso_neto, '.2f'))

    print('
CANTIDAD DE SERVICIOS ATENDIDOS')
    total_vehiculos = 0
    for servicio in contador_servicios:
        cantidad = contador_servicios[servicio]
        print(f'- {servicio}: {cantidad}')
        total_vehiculos = total_vehiculos + cantidad

    print('------------------------------------------------')
    print('Total general de vehiculos atendidos:', total_vehiculos)
    print('================================================')

