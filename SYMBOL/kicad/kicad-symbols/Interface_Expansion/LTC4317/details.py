
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "LTC4317"
    hexID = "SZKINTERFACEEXPANSIONLTC4317"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4317', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-16-1EP_3x5mm_P0.5mm_EP1.66x4.4mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/4317fa.pdf', 'kicadSymbolki_keywords': 'I2C Translator 4kV-ESD Level-Shifter Hot-Swap', 'kicadSymbolki_description': 'Dual I2C/SMBus Address-Translator, DFN-16', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x5mm*P0.5mm*'}])
    newPart['name'].append('Interface_Expansion : LTC4317')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

