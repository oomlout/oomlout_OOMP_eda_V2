
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "FT4232H"
    hexID = "SZKINTERFACEUFT4232H"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FT4232H', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT4232H.pdf', 'kicadSymbolki_keywords': 'FTDI USB Quad UART FIFO', 'kicadSymbolki_description': 'Hi Speed Quad Channel USB UART/FIFO, LQFP/QFN-64', 'kicadSymbolki_fp_filters': 'QFN*1EP*9x9mm*P0.5mm* LQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('Interface_USB : FT4232H')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

