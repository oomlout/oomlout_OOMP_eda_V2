
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "MAX6654"
    hexID = "SZKSENTEMPERATUREMAX6654"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX6654', 'kicadSymbolFootprint': 'Package_SO:SSOP-16_3.9x4.9mm_P0.635mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX6654.pdf', 'kicadSymbolki_keywords': 'I2C SMBus Serial', 'kicadSymbolki_description': 'Remote and Local Temperature Sensor, SSOP-16', 'kicadSymbolki_fp_filters': '*SOP*3.9x4.9mm*P0.635mm*'}])
    newPart['name'].append('Sensor_Temperature : MAX6654')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

