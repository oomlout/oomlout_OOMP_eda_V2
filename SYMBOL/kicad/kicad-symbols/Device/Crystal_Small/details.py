
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Crystal_Small"
    hexID = "SZKDEVICEXSLL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Y', 'kicadSymbolValue': 'Crystal_Small', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'quartz ceramic resonator oscillator', 'kicadSymbolki_description': 'Two pin crystal, small symbol', 'kicadSymbolki_fp_filters': 'Crystal*'}])
    newPart['name'].append('Device : Crystal_Small')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

