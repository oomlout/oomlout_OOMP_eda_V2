
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "TB5D2H"
    hexID = "SZKINTERFACETB5D2H"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TB5D1MD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TB5D2H', 'kicadSymbolFootprint': 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tb5d2h.pdf', 'kicadSymbolki_keywords': 'differential PECL driver', 'kicadSymbolki_description': 'Quad differential PECL driver', 'kicadSymbolki_fp_filters': 'SOIC*3.9x9.9mm*P1.27*'}])
    newPart['name'].append('Interface : TB5D2H')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

