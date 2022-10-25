
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "PCA9547PW"
    hexID = "SZKINTERFACEEXPANSIONPCA9547PW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PCA9548ADB', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCA9547PW', 'kicadSymbolFootprint': 'Package_SO:TSSOP-24_4.4x7.8mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/PCA9547.pdf', 'kicadSymbolki_keywords': 'Low voltage 8-channel I2C switch with reset', 'kicadSymbolki_description': 'Low voltage 8-channel I2C switch with reset, TSSOP-24', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x7.8mm*P0.65mm*'}])
    newPart['name'].append('Interface_Expansion : PCA9547PW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

