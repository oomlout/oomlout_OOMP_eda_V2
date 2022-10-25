
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "MCP9700AT-HLT"
    hexID = "SZKSENTEMPERATUREMCP97ATHLT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP9700AT-ELT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP9700AT-HLT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21942e.pdf', 'kicadSymbolki_keywords': 'temperature sensor thermistor', 'kicadSymbolki_description': 'Low power, analog thermistor temperature sensor, ±2C accuracy, -40C to +150C, in SC-70-5', 'kicadSymbolki_fp_filters': 'SC-70-5*'}])
    newPart['name'].append('Sensor_Temperature : MCP9700AT-HLT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

