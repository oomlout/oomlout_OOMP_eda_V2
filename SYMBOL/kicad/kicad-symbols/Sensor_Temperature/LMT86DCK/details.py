
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "LMT86DCK"
    hexID = "SZKSENTEMPERATURELMT86DCK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMT86DCK', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmt86-q1.pdf', 'kicadSymbolki_keywords': 'temperature sensor thermistor ntc', 'kicadSymbolki_description': 'Analog temperature sensor, NTC, 0.25C accuracy, -10.9mV/C, -50C to +150C, 2.2 to 5.5V, SC-70-5', 'kicadSymbolki_fp_filters': 'SC-70-*'}])
    newPart['name'].append('Sensor_Temperature : LMT86DCK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

