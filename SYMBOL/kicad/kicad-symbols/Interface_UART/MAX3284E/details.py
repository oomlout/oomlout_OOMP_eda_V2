
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "MAX3284E"
    hexID = "SZKINTERFACEUARTMAX3284E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX3284E', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX3280E-MAX3284E.pdf', 'kicadSymbolki_keywords': 'RS-485 RS-422 True Fail-Safe Receivers 1/4 unit load receiver', 'kicadSymbolki_description': '±15kV ESD-Protected 52Mbps, 3V to 5.5V RS-485/RS-422 True Fail-Safe Receivers, SOT23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Interface_UART : MAX3284E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

