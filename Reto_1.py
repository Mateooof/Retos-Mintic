"""
Created on Sun May  1 19:18:19 2022

@author: MATEO
"""
"""
Este primer reto consiste en crear un función con nombre CDT, la cual recibe como parametros el nombre del usuario (el cual es un caracter alfanumerico),
la cantidad de capital y el tiempo en meses. 
Esta función calcula el valor total del dinero al guardarlo en un CDT una cierta cantidad de meses.

"""

def CDT(usuario:str,capital:int,tiempo:int):
    """
    Parameters
    ----------
    usuario : str
        Alfanumerico que identifica el usuario
    capital : int
        Monto a ingresar
    tiempo : int
        Tiempo del CDT en meses

    Returns
    -------
    Ganancias o pérdidas generadas, a manera de un texto organizado
    “Para el usuario {} La cantidad de dinero a recibir, según el monto
    inicial {} para un tiempo de {} meses es: {}”

    """
    if tiempo > 2:
        valor_intereses = (capital*0.03*tiempo)/12
        valor_total = valor_intereses + capital
        texto_final= f"Para el usuario {usuario}. La cantidad de dinero a recibir, según el monto inicial de ${capital} para un tiempo de {tiempo} meses es de: ${valor_total}"
        return texto_final
    elif tiempo > 0 and tiempo <=2:
        valor_a_perder=capital*0.02
        valor_total= capital-valor_a_perder
        texto_final=f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}"
        return texto_final
    else:
        texto_final=f"Datos incorrectos"
        return texto_final
        
