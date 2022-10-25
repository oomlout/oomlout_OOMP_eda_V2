
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "TLV7041DBV"
    hexID = "SZKCOMPARATORTLV741DBV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP6566', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV7041DBV', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/tlv7041.pdf', 'kicadSymbolki_keywords': 'cmp collector', 'kicadSymbolki_description': 'Single, 1.6V-6.5V, 315nA Quiescent, Open-Drain Output, Comparator, SOT-23-5/SC-70', 'kicadSymbolki_fp_filters': 'SOT?23* *SC*70*'}])
    newPart['name'].append('Comparator : TLV7041DBV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

