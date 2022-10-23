
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "FT232H"
    hexID = "SZKINTERFACEUFT232H"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FT232H', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT232H.pdf', 'kicadSymbolki_keywords': 'FTDI USB Single UART FIFO', 'kicadSymbolki_description': 'Hi Speed Single Channel USB UART/FIFO, LQFP/QFN-48', 'kicadSymbolki_fp_filters': 'QFN*1EP*8x8mm*P0.5mm* LQFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('FT232H')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

