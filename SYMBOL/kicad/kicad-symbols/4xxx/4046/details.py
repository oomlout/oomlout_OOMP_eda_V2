
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "4xxx"
    oIndex = "4046"
    hexID = "SZK4XXX446"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '4046', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/HEF4046B.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'CMOS PLL', 'kicadSymbolki_description': 'Phase Comp & VCO', 'kicadSymbolki_fp_filters': 'DIP?16*'}])
    newPart['name'].append('4xxx : 4046')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

