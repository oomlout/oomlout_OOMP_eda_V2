
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "1N4148WS"
    hexID = "SZKDIODE1N4148WS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '1N4001', 'kicadSymbolReference': 'D', 'kicadSymbolValue': '1N4148WS', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-323', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/85751/1n4148ws.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '75V 0.15A Fast switching Diode, SOD-323', 'kicadSymbolki_fp_filters': 'D*SOD?323*'}])
    newPart['name'].append('Diode : 1N4148WS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

