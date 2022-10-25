
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "MAX13432EETD"
    hexID = "SZKINTERFACEUARTMAX13432EETD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX13432EETD', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-14-1EP_3x3mm_P0.4mm_EP1.78x2.35mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX13430E-MAX13433E.pdf', 'kicadSymbolki_keywords': 'rs485 transceiver', 'kicadSymbolki_description': 'RS485 transceiver, full duplex, dual supply, receiver/driver enable, 500kbps, DFN-14 package', 'kicadSymbolki_fp_filters': 'DFN*3x3mm*P0.4mm*'}])
    newPart['name'].append('Interface_UART : MAX13432EETD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

