
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS22"
    hexID = "SZK74XX74LS22"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LS20', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS22', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74LS22', 'kicadSymbolki_keywords': 'TTL Nand4 OpenColl', 'kicadSymbolki_description': 'Dual 4-input NAND Open Collector', 'kicadSymbolki_fp_filters': 'DIP?12*'}])
    newPart['name'].append('74xx : 74LS22')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

