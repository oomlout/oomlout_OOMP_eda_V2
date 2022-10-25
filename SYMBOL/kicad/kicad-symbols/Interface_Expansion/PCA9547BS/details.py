
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "PCA9547BS"
    hexID = "SZKINTERFACEEXPANSIONPCA9547BS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCA9547BS', 'kicadSymbolFootprint': 'Package_DFN_QFN:HVQFN-24-1EP_4x4mm_P0.5mm_EP2.1x2.1mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/PCA9547.pdf', 'kicadSymbolki_keywords': 'Low voltage 8-channel I2C switch with reset', 'kicadSymbolki_description': 'Low voltage 8-channel I2C switch with reset, HVQFN-24', 'kicadSymbolki_fp_filters': 'HVQFN*4x4mm*P0.5mm*'}])
    newPart['name'].append('Interface_Expansion : PCA9547BS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

