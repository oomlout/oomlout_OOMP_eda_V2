
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xGxx"
    oIndex = "74LVC2G14"
    hexID = "SZK74XGXX74LVC2G14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LVC2G14', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/sn74lvc2g14.pdf', 'kicadSymbolki_keywords': 'Dual Gate NOT Schmitt LVC CMOS', 'kicadSymbolki_description': 'Dual NOT Gate Schmitt Triggered, Low-Voltage CMOS', 'kicadSymbolki_fp_filters': 'SG-* SOT*'}])
    newPart['name'].append('74xGxx : 74LVC2G14')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

