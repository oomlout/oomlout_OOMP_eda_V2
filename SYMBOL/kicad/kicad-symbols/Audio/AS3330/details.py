
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "AS3330"
    hexID = "SZKAUDIOAS333"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AS3330', 'kicadSymbolFootprint': 'Package_DIP:DIP-18_W7.62mm', 'kicadSymbolDatasheet': 'http://www.alfarzpp.lv/eng/sc/AS3330.pdf', 'kicadSymbolki_keywords': 'VCA CEM3330 ALFA', 'kicadSymbolki_description': 'Dual Voltage Controlled Amplifier (VCA), DIP-18', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Audio : AS3330')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

