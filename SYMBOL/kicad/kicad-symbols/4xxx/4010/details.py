
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "4xxx"
    oIndex = "4010"
    hexID = "SZK4XXX41"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '4010', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/cd4010b-q1.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'CMOS BUFFER high sink, VCC and VDD sep. VDD>VI>VCC!', 'kicadSymbolki_description': 'Hex Buffer', 'kicadSymbolki_fp_filters': 'DIP?16*'}])
    newPart['name'].append('4xxx : 4010')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

