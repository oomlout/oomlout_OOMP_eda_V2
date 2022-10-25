
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "LMT84DCK"
    hexID = "SZKSENTEMPERATURELMT84DCK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMT84DCK', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmt84.pdf', 'kicadSymbolki_keywords': 'temperature sensor thermistor ntc', 'kicadSymbolki_description': 'Analog temperature sensor, NTC, 0.4C accuracy, -5.5mV/C, -50C to +150C, 1.5 to 5.5V, SC-70-5', 'kicadSymbolki_fp_filters': 'SC-70-*'}])
    newPart['name'].append('Sensor_Temperature : LMT84DCK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

