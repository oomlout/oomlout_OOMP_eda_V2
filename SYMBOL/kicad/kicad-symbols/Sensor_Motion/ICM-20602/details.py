
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "ICM-20602"
    hexID = "SZKSENMOTIONICM262"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ICM-20602', 'kicadSymbolFootprint': 'Package_LGA:LGA-16_3x3mm_P0.5mm_LayoutBorder3x5y', 'kicadSymbolDatasheet': 'http://www.invensense.com/wp-content/uploads/2016/10/DS-000176-ICM-20602-v1.0.pdf', 'kicadSymbolki_keywords': 'accelerometer gyro mems motion', 'kicadSymbolki_description': 'High performance 6-Axis MEMS motion tracking, SPI/I2C interface, LGA-16', 'kicadSymbolki_fp_filters': 'LGA*3x3mm*P0.5mm*'}])
    newPart['name'].append('Sensor_Motion : ICM-20602')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

