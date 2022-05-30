def AutoPartes(ventas: list):
    # Inicializar diccionario
    venta = dict()
    # Ciclo para agregar un nuevo evento
    for idProducto, dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta in ventas:
        # Fuerza la entrada
        if venta.get(idProducto) is None:
            # Creacion de un nuevo evento
            venta[idProducto] = []
            # Registro de una nueva lista de tuplas en el dict agenda
        venta[idProducto].append((dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta))
    return venta
    

def consultaRegistro(ventas, idProducto):
    if idProducto in ventas.keys():
        for dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta in ventas[idProducto]:
            return print(
                f"Producto consultado : {idProducto}  Descripción  {dProducto}  #Parte  {pnProducto}  Cantidad vendida  {cvProducto}  Stock  {sProducto}  Comprador {nComprador}  Documento  {cComprador}  Fecha Venta  {fVenta}\n"

            )
            
    else:
        return print("No hay registro de venta de ese producto")

# Datos solo para Pruebas
consultaRegistro(AutoPartes([
    (5489,'tornillo', 'RS8512',2,33,'Julio Perez',3654213,'13/06/2020'),
    (2001,'zocalo', 'UM8587',2,125,'Laura Macias',1256321,'13/06/2020'),
    (3698,'biela', 'PT3218',1,78,'Luis Peña',14565487,'13/06/2020'),
    (2001,'cilindro', 'AZ8794',2,96,'Carlos Casio',5612405,'13/06/2020')]), 2001)
print()


