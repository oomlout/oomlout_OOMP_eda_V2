
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Valve"
    oIndex = "6AK8"
    hexID = "SZKVA6AK8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'EABC80', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '6AK8', 'kicadSymbolFootprint': 'Valve:Valve_Noval_P', 'kicadSymbolDatasheet': 'https://frank.pocnet.net/sheets/082/e/EABC80.pdf', 'kicadSymbolki_keywords': 'diode triode valve', 'kicadSymbolki_description': 'triple diode triode', 'kicadSymbolki_fp_filters': 'VALVE*NOVAL*P*'}])
    newPart['name'].append('Valve : 6AK8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

