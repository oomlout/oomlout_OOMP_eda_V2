
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "AS3360"
    hexID = "SZKAUDIOAS336"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AS3360', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.alfarzpp.lv/eng/sc/AS3360.pdf', 'kicadSymbolki_keywords': 'VCA CEM3360 ALFA', 'kicadSymbolki_description': 'Dual Voltage Controlled Amplifier (VCA), DIP-14/SOIC-14', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('Audio : AS3360')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

