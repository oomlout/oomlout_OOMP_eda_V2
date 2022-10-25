
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "FT4222HQ"
    hexID = "SZKINTERFACEUFT4222HQ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FT4222HQ', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm', 'kicadSymbolDatasheet': 'https://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT4222H.pdf', 'kicadSymbolki_keywords': 'USB SPI I2C FTDI Bridge Converter Interface', 'kicadSymbolki_description': 'USB 2.0 to Quad SPI or I2C Bridge, VQFN-32', 'kicadSymbolki_fp_filters': 'VQFN*5x5mm*P0.5mm*'}])
    newPart['name'].append('Interface_USB : FT4222HQ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

