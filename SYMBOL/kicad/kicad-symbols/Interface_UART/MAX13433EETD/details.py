
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "MAX13433EETD"
    hexID = "SZKINTERFACEUARTMAX13433EETD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX13432EETD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX13433EETD', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-14-1EP_3x3mm_P0.4mm_EP1.78x2.35mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX13430E-MAX13433E.pdf', 'kicadSymbolki_keywords': 'rs485 transceiver', 'kicadSymbolki_description': 'RS485 transceiver, full duplex, dual supply, receiver/driver enable, 16Mbps, DFN-14 package', 'kicadSymbolki_fp_filters': 'DFN*3x3mm*P0.4mm*'}])
    newPart['name'].append('MAX13433EETD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

