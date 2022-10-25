
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "TC1047xNB"
    hexID = "SZKSENTEMPERATURETC147XNB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP9700T-HTT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TC1047xNB', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21498D.pdf', 'kicadSymbolki_keywords': 'temperature sensor analog', 'kicadSymbolki_description': 'Precision Temperature-to-Voltage Converter, 10mV/ºC, -40ºC to +125ºC, ±2.0ºC (max), 2.7V to 4.4V, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Sensor_Temperature : TC1047xNB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

