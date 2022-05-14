def cliente(informacion: dict) -> dict:
    data = dict()
    apto = True
    if informacion['edad'] > 18:
        atraccion = 'X-Treme'
        if informacion['primer_ingreso']:
            valor_boleta = 20000 * 0.95
        else:
            valor_boleta = 20000
    elif 15 <= informacion['edad'] <= 18:
        atraccion = 'Carros chocones'
        if informacion['primer_ingreso']:
            valor_boleta = 5000 * 0.93
        else:
            valor_boleta = 5000
    elif 7 <= informacion['edad'] < 15:
        atraccion = 'Sillas voladoras'
        if informacion['primer_ingreso']:
            valor_boleta = 10000 * 0.95
        else:
            valor_boleta = 10000
    else:
        apto = False
        valor_boleta = 'N/A'
        atraccion = 'N/A'

    data['nombre'] = informacion['nombre']
    data['edad'] = informacion['edad']
    data['atraccion'] = atraccion
    data['apto'] = apto
    data['primer_ingreso'] = informacion['primer_ingreso']
    data['total_boleta'] = valor_boleta

    return data


# Datos Test
data_test = {'id': '3', 'nombre': 'Gloria Suarez', 'edad': 3, 'primer_ingreso': True}
print(cliente(data_test))

