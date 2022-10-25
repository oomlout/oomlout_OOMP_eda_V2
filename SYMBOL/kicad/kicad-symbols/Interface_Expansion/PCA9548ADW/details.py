
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "PCA9548ADW"
    hexID = "SZKINTERFACEEXPANSIONPCA9548ADW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCA9548ADW', 'kicadSymbolFootprint': 'Package_SO:SOIC-24W_7.5x15.4mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/pca9548a.pdf', 'kicadSymbolki_keywords': 'Low voltage 8-channel I2C switch with reset', 'kicadSymbolki_description': 'Low voltage 8-channel I2C switch with reset, SOIC-24', 'kicadSymbolki_fp_filters': 'SOIC*7.5x15.4mm*P1.27mm*'}])
    newPart['name'].append('Interface_Expansion : PCA9548ADW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

