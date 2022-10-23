
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "TB5R2D"
    hexID = "SZKINTERFACETB5R2D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TB5R1D', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TB5R2D', 'kicadSymbolFootprint': 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tb5r1.pdf', 'kicadSymbolki_keywords': 'differential PECL reciver', 'kicadSymbolki_description': 'Quad differential PECL reciver', 'kicadSymbolki_fp_filters': 'SOIC*3.9x9.9mm*P1.27*'}])
    newPart['name'].append('TB5R2D')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

