
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "4xxx"
    oIndex = "4016"
    hexID = "SZK4XXX416"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '4016', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/cd4016b.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'CMOS SWITCH', 'kicadSymbolki_description': 'Quad Analog Switches', 'kicadSymbolki_fp_filters': 'DIP?14*'}])
    newPart['name'].append('4xxx : 4016')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

