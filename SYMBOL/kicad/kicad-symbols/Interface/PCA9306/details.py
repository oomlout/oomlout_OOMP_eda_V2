
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "PCA9306"
    hexID = "SZKINTERFACEPCA936"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCA9306', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/pca9306.pdf', 'kicadSymbolki_keywords': 'Dual bidirectional I2C Bus and SMBus voltage level translator', 'kicadSymbolki_description': 'Dual bidirectional I2C Bus and SMBus voltage level translator', 'kicadSymbolki_fp_filters': 'SSOP*2.95x2.8mm*P0.65mm* VSSOP*2.3x2mm*P0.5mm* X2SON*1.4x1mm*P0.35mm*'}])
    newPart['name'].append('Interface : PCA9306')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

