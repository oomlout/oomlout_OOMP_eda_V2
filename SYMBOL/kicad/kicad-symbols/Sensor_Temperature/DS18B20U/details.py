
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "DS18B20U"
    hexID = "SZKSENTEMPERATUREDS18B2U"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DS18B20U', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/DS18B20.pdf', 'kicadSymbolki_keywords': 'OneWire 1-Wire 1Wire Maxim Dallas', 'kicadSymbolki_description': 'Programmable Resolution 1-Wire Digital Thermometer MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Sensor_Temperature : DS18B20U')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

