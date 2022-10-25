
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "LTC4314xUDC"
    hexID = "SZKINTERFACEEXPANSIONLTC4314XUDC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4314xUDC', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-20-1EP_3x4mm_P0.5mm_EP1.65x2.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/4314f.pdf', 'kicadSymbolki_keywords': 'I2C Multiplexer Buffer Level Shifter', 'kicadSymbolki_description': 'Pin-Selectable, 4-Channel, 2-Wire Multiplexer with Bus Buffers, QFN-20', 'kicadSymbolki_fp_filters': 'QFN*1EP*3x4mm*P0.5mm*'}])
    newPart['name'].append('Interface_Expansion : LTC4314xUDC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

