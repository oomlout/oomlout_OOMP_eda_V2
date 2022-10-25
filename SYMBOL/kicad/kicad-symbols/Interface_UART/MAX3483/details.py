
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "MAX3483"
    hexID = "SZKINTERFACEUARTMAX3483"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX481E', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX3483', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX3483-MAX3491.pdf', 'kicadSymbolki_keywords': 'RS-485 RS-422 UART line-driver transceiver', 'kicadSymbolki_description': 'True RS-485/RS-422, 0.25Mbps, Slew-Rate Limited, with low-power shutdown, with receiver/driver enable, 32 receiver drive capacitity, DIP-8 and SOIC-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Interface_UART : MAX3483')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

