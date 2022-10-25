
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "DS18B20Z"
    hexID = "SZKSENTEMPERATUREDS18B2Z"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DS1822Z', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DS18B20Z', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/DS18B20.pdf', 'kicadSymbolki_keywords': 'OneWire 1Wire Maxim Dallas', 'kicadSymbolki_description': 'Programmable Resolution 1-Wire Digital Thermometer SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Sensor_Temperature : DS18B20Z')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

