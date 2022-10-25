
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "PCA9306DP"
    hexID = "SZKINTERFACEPCA936DP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PCA9306', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCA9306DP', 'kicadSymbolFootprint': 'Package_SO:TSSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/PCA9306.pdf', 'kicadSymbolki_keywords': 'I2C SMBus', 'kicadSymbolki_description': 'Dual bidirectional I2C Bus and SMBus voltage level translator, TSSOP-8', 'kicadSymbolki_fp_filters': 'TSSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Interface : PCA9306DP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

