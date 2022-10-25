
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xGxx"
    oIndex = "74AUP1G32"
    hexID = "SZK74XGXX74AUP1G32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LVC1G32', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74AUP1G32', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf', 'kicadSymbolki_keywords': 'Single Gate OR LVC CMOS', 'kicadSymbolki_description': 'Single OR Gate, Low-Voltage CMOS', 'kicadSymbolki_fp_filters': 'SOT* SG-*'}])
    newPart['name'].append('74xGxx : 74AUP1G32')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

