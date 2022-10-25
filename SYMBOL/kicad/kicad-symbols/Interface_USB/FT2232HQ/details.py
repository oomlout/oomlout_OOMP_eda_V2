
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "FT2232HQ"
    hexID = "SZKINTERFACEUFT2232HQ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FT2232HQ', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-64-1EP_9x9mm_P0.5mm_EP4.35x4.35mm', 'kicadSymbolDatasheet': 'https://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT2232H.pdf', 'kicadSymbolki_keywords': 'USB Double UART FIFO', 'kicadSymbolki_description': 'Hi Speed Double Channel USB UART/FIFO, QFN-64', 'kicadSymbolki_fp_filters': 'QFN*1EP*9x9mm*P0.5mm*'}])
    newPart['name'].append('Interface_USB : FT2232HQ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

