from sympy import E, true


def cliente(informacion:dict):
    if informacion["edad"]>18:
        apto= True
        atraccion= "X-Treme"
        if informacion["primer_ingreso"]== True:
            valor_boleta= (20000*95)/100
        else:
            valor_boleta= 20000
    elif informacion["edad"] >= 15 and informacion["edad"] <=18:
        apto=True
        atraccion="Carros chocones"
        if informacion["primer_ingreso"]== True:
            valor_boleta=(5000*93)/100
        else:
            valor_boleta= 5000
    elif informacion["edad"] >=7 and informacion["edad"] <15:
        apto=True
        atraccion= "Sillas voladoras"
        if informacion["primer_ingreso"]== True:
            valor_boleta = (10000*95)/100
        else:
            valor_boleta=10000
    else:
        apto=False
        atraccion="N/A"
        valor_boleta="N/A"
        
    return {"nombre":informacion["nombre"],"edad":informacion["edad"],"atraccion": atraccion,"apto":apto,"primer_ingreso":informacion["primer_ingreso"],"total_boleta":valor_boleta}
informacion={"id_cliente":3,"nombre":"Tatiana Suarez","edad":17,"primer_ingreso":True}
print(cliente(informacion))
