
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "TB5R2DW"
    hexID = "SZKINTERFACETB5R2DW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TB5R1DW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TB5R2DW', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tb5r1.pdf', 'kicadSymbolki_keywords': 'differential PECL reciver', 'kicadSymbolki_description': 'Quad differential PECL reciver', 'kicadSymbolki_fp_filters': 'SOIC*7.5x10.3mm*P1.27*'}])
    newPart['name'].append('Interface : TB5R2DW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

