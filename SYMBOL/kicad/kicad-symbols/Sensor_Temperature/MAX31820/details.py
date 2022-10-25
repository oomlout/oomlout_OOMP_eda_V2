
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "MAX31820"
    hexID = "SZKSENTEMPERATUREMAX3182"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX31820', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/MAX31820.pdf', 'kicadSymbolki_keywords': 'OneWire 1-Wire 1Wire Maxim Dallas', 'kicadSymbolki_description': '1-Wire Ambient Temperature Sensor TO-92', 'kicadSymbolki_fp_filters': 'TO*92*'}])
    newPart['name'].append('Sensor_Temperature : MAX31820')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

