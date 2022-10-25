
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "TMP20AIDRL"
    hexID = "SZKSENTEMPERATURETMP2AIDRL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TMP20AIDRL', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tmp20.pdf', 'kicadSymbolki_keywords': 'temperature sensor thermistor', 'kicadSymbolki_description': 'Analog thermistor temperature sensor, ±2.5C accuracy, -55C to +130C, SOT-563-6', 'kicadSymbolki_fp_filters': 'SOT?563*'}])
    newPart['name'].append('Sensor_Temperature : TMP20AIDRL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

