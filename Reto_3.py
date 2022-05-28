def AutoPartes(ventas:list):
    registro={}
    for i in range(len(ventas)):
        registro[i]=[ventas[i]]
    return registro
def consultaRegistro(ventas, idProducto:int):
    registro2={}
    for i in ventas:
        if ventas[i][0][0]== idProducto:
            registro2[i]=ventas[i]
    m=""
    if len(registro2)==0:
        m="No hay registro de venta de ese producto"
    else:
        for i in registro2: 
            m+="Producto consultado : {}  Descripción  {}  #Parte  {}  Cantidad vendida  {}  Stock  {}  Comprador {}  Documento  {}  Fecha Venta  {}\n".format(ventas[i][0][0],ventas[i][0][1],ventas[i][0][2],ventas[i][0][3],ventas[i][0][4],ventas[i][0][5],ventas[i][0][6],ventas[i][0][7])
    return print(m)
