
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "MAX40200AUK"
    hexID = "SZKANALOGSWITCHMAX42AUK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX40200AUK', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX40200.pdf', 'kicadSymbolki_keywords': 'current switch', 'kicadSymbolki_description': 'Ideal Diode, Ultra-Low Voltage Drop, 1.5-5.5V, 1A, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Analog_Switch : MAX40200AUK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

