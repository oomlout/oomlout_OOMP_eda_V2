
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "FT2232D"
    hexID = "SZKINTERFACEUFT2232D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FT2232D', 'kicadSymbolFootprint': 'Package_QFP:LQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT2232D.pdf', 'kicadSymbolki_keywords': 'USB Double UART FIFO', 'kicadSymbolki_description': 'Full Speed Double Channel USB UART/FIFO, LQFP-48', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('Interface_USB : FT2232D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

