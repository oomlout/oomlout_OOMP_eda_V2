
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "PCA9557D"
    hexID = "SZKINTERFACEEXPANSIONPCA9557D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCA9557D', 'kicadSymbolFootprint': 'Package_SO:SO-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/PCA9557.pdf', 'kicadSymbolki_keywords': 'SMBUS I2C Expander', 'kicadSymbolki_description': '8-bit I2C-bus and SMBus I/O port with reset, SO-16', 'kicadSymbolki_fp_filters': 'SO*3.9x9.9mm*P1.27mm*'}])
    newPart['name'].append('Interface_Expansion : PCA9557D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

