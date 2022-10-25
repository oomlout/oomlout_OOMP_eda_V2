
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Resonator"
    hexID = "SZKDEVICER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Y', 'kicadSymbolValue': 'Resonator', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'ceramic resonator', 'kicadSymbolki_description': 'Three pin ceramic resonator', 'kicadSymbolki_fp_filters': 'Filter* Resonator*'}])
    newPart['name'].append('Device : Resonator')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

