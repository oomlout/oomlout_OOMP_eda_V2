
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "PCA9306DC"
    hexID = "SZKINTERFACEPCA936DC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PCA9306', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCA9306DC', 'kicadSymbolFootprint': 'Package_SO:VSSOP-8_2.3x2mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/PCA9306.pdf', 'kicadSymbolki_keywords': 'I2C SMBus', 'kicadSymbolki_description': 'Dual bidirectional I2C Bus and SMBus voltage level translator, VSSOP-8, Discontinued', 'kicadSymbolki_fp_filters': 'VSSOP*2.3x2mm*P0.5mm*'}])
    newPart['name'].append('Interface : PCA9306DC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

