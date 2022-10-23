
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Ethernet"
    oIndex = "ENC424J600-ML"
    hexID = "SZKINTERFACEETHERNETENC424J6ML"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ENC424J600-ML', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-44-1EP_8x8mm_P0.65mm_EP6.45x6.45mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39935c.pdf', 'kicadSymbolki_keywords': 'ENC Ethernet', 'kicadSymbolki_description': 'Stand-Alone 10/100 Ethernet Controller with SPI or Parallel Interface, QFN-44', 'kicadSymbolki_fp_filters': 'QFN*44*8x8mm*P0.65mm*'}])
    newPart['name'].append('ENC424J600-ML')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

