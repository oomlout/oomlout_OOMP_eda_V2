
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "TSSP58038"
    hexID = "SZKSENPROXIMITYTSSP5838"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TSSP58P38', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSSP58038', 'kicadSymbolFootprint': 'OptoDevice:Vishay_MINICAST-3Pin', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/82476/tssp58p38.pdf', 'kicadSymbolki_keywords': 'opto IR receiver proximity sensor', 'kicadSymbolki_description': 'IR Detector for Mid Range Proximity Sensor', 'kicadSymbolki_fp_filters': 'Vishay*MINICAST*'}])
    newPart['name'].append('Sensor_Proximity : TSSP58038')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

