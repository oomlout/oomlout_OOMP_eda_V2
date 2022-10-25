
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "PCA9537"
    hexID = "SZKINTERFACEEXPANSIONPCA9537"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCA9537', 'kicadSymbolFootprint': 'Package_SO:TSSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/PCA9537.pdf', 'kicadSymbolki_keywords': 'i2c io port', 'kicadSymbolki_description': '4-bit I2C-bus and SMBus IO port with interrupt and reset, TSSOP-10', 'kicadSymbolki_fp_filters': 'TSSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Interface_Expansion : PCA9537')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

