
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "TSSP58038SS1XB"
    hexID = "SZKSENPROXIMITYTSSP5838SS1XB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TSSP58P38', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSSP58038SS1XB', 'kicadSymbolFootprint': 'OptoDevice:Vishay_MINICAST-3Pin', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/82740/tssp58038ss1xb.pdf', 'kicadSymbolki_keywords': 'opto IR receiver light barrier', 'kicadSymbolki_description': 'IR Receiver Module for Light Barrier Systems', 'kicadSymbolki_fp_filters': 'Vishay*MINICAST*'}])
    newPart['name'].append('Sensor_Proximity : TSSP58038SS1XB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

