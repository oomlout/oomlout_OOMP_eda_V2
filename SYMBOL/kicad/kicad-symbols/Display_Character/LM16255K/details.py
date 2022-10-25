
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "LM16255K"
    hexID = "SZKDICHARACTERLM16255K"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM16255K', 'kicadSymbolFootprint': 'Display:LM16255', 'kicadSymbolDatasheet': 'http://pdf.datasheetcatalog.com/datasheet/Sharp/mXvtrzw.pdf', 'kicadSymbolki_keywords': 'display LCD dot-matrix', 'kicadSymbolki_description': '2 Lines, 12 character reflective LCD', 'kicadSymbolki_fp_filters': '*LM16255*'}])
    newPart['name'].append('Display_Character : LM16255K')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

