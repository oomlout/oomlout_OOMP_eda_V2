
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xGxx"
    oIndex = "74LVC2G00"
    hexID = "SZK74XGXX74LVC2G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LVC2G00', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf', 'kicadSymbolki_keywords': 'Dual Gate NAND LVC CMOS', 'kicadSymbolki_description': 'Dual NAND Gate, Low-Voltage CMOS', 'kicadSymbolki_fp_filters': 'SSOP* VSSOP*'}])
    newPart['name'].append('74xGxx : 74LVC2G00')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

