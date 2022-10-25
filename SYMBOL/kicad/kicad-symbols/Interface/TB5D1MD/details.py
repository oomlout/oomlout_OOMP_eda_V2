
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "TB5D1MD"
    hexID = "SZKINTERFACETB5D1MD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TB5D1MD', 'kicadSymbolFootprint': 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tb5d2h.pdf', 'kicadSymbolki_keywords': 'differential PECL driver', 'kicadSymbolki_description': 'Quad differential PECL driver', 'kicadSymbolki_fp_filters': 'SOIC*3.9x9.9mm*P1.27*'}])
    newPart['name'].append('Interface : TB5D1MD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

