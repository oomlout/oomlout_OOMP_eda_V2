
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "MCP4251-xxxx-ML"
    hexID = "SZKPOTENTIOMETERDIGITALMCP4251XXXXML"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP4251-xxxx-ML', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_4x4mm_P0.65mm_EP2.5x2.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/22060b.pdf', 'kicadSymbolki_keywords': 'Digital Pot Potentiometer', 'kicadSymbolki_description': 'Dual 8 Bit Digital Pot, SPI, Volatile Memory, QFN-16', 'kicadSymbolki_fp_filters': 'QFN*4x4mm*P0.65mm*'}])
    newPart['name'].append('MCP4251-xxxx-ML')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

