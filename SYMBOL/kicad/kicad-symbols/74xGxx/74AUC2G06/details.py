
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xGxx"
    oIndex = "74AUC2G06"
    hexID = "SZK74XGXX74AUC2G6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LVC2G06', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74AUC2G06', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf', 'kicadSymbolki_keywords': 'Dual Gate NOT Open Drain LVC CMOS', 'kicadSymbolki_description': 'Dual NOT Gate w/ Open Drain, Low-Voltage CMOS', 'kicadSymbolki_fp_filters': 'SG-* SOT*'}])
    newPart['name'].append('74xGxx : 74AUC2G06')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

