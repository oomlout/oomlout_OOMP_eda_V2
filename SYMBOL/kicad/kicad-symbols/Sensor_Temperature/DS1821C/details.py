
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "DS1821C"
    hexID = "SZKSENTEMPERATUREDS1821C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX31820', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DS1821C', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/DS1821.pdf', 'kicadSymbolki_keywords': 'OneWire 1Wire Maxim Dallas', 'kicadSymbolki_description': 'Programmable Digital Thermostat and Thermometer TO-92', 'kicadSymbolki_fp_filters': 'TO*92*'}])
    newPart['name'].append('Sensor_Temperature : DS1821C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

