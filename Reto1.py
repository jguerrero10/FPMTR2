"""
Descripción del problema:

Una entidad Bancaria o entidad financiera, requiere calcular el valor de los intereses ganados y el total final de
dinero para diferentes clientes, de acuerdo, a una cantidad de dinero invertida en un CDT. Un CDT por su parte, es un
producto financiero que ofrece la posibilidad de guardar dinero durante un tiempo determinado para recibir
posteriormente sus intereses devengados, asimismo, ofrece rendimientos a una tasa fija, asegurando una rentabilidad
libre de riesgo en un tiempo determinado que por lo general debe ser mayor a dos (2) meses. Si, este dinero se retira
antes de este periodo se aplica una penalidad del 2%.

En ese sentido, el valor de los intereses ganados por un periodo de tiempo superior a dos meses se determina a través
de la siguiente formula:

valor_intereses = Cantidad * porcentaje_interes * Tiempo / 12

Donde:
cantidad = dinero ingresado en el CDT
porcentaje_interes = 3% (0.03).
tiempo = cantidad de tiempo

En consecuencia, el valor total del dinero será calculado a través de la siguiente formula:

Valor_total = valor_intereses + cantidad

Se debe determinar el valor total a retirar por el cliente que invirtió en el CDT al final del periodo.

Por otra parte, para un periodo de tiempo inferior o igual a dos meses se debe aplicar la siguiente formula:

valor_perder = cantidad * porcentaje_perder

Donde:
cantidad = dinero ingresado en el CDT
procentajea_perder = 2% (0.02)

En consecuencia, el valor total del dinero será calculado a través de la siguiente formula:

Valor_total = cantidad - valor_perder

Para responder a este planteamiento, escriba una función que reciba como parámetros: una cadena con el usuario del
cliente como dato alfanumérico, el capital aportado y el tiempo del CDT y, en consecuencia, retorne una cadena de
caracteres que le proporcione al banco la información que desea obtener.
La cadena debe tener para el caso de las ganancias, la siguiente estructura:
“Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}”
para el caso de las pérdidas:
“Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}”
"""


def cdt(usuario: str, capital: int, tiempo: int):
    porcentaje_interes = 0.03
    if tiempo > 2:
        valor_intereses = capital * porcentaje_interes * tiempo / 12
        valor_total = valor_intereses + capital
        resultado = f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} " \
                    f"para un tiempo de {tiempo} meses es: {valor_total}"
    else:
        porcentaje_perder = 0.02
        valor_perder = capital * porcentaje_perder
        valor_total = capital - valor_perder
        resultado = f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} " \
                    f"para un tiempo de {tiempo} meses es: {valor_total}"
    return resultado


# Solo para Pruebas
print(cdt('AB1012', 1000000, 3))
