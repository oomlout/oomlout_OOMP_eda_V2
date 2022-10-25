
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "FT201XQ"
    hexID = "SZKINTERFACEUFT21XQ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FT201XQ', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_4x4mm_P0.65mm_EP2.1x2.1mm', 'kicadSymbolDatasheet': 'https://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT201X.pdf', 'kicadSymbolki_keywords': 'FTDI USB I2C interface Converter', 'kicadSymbolki_description': 'Full Speed USB to I2C Bridge, QFN-10', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.65mm*'}])
    newPart['name'].append('Interface_USB : FT201XQ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

