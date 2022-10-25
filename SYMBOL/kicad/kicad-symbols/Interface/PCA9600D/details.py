
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "PCA9600D"
    hexID = "SZKINTERFACEPCA96D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCA9600D', 'kicadSymbolFootprint': 'Package_SO:SO-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/PCA9600.pdf', 'kicadSymbolki_keywords': 'I2C buffer', 'kicadSymbolki_description': 'Dual bidirectional bus buffer, SO-8', 'kicadSymbolki_fp_filters': 'SO*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Interface : PCA9600D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

