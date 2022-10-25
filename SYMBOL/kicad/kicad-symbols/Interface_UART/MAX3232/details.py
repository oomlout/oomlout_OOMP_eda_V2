
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "MAX3232"
    hexID = "SZKINTERFACEUARTMAX3232"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX232', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX3232', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX3222-MAX3241.pdf', 'kicadSymbolki_keywords': 'rs232 uart transceiver line-driver', 'kicadSymbolki_description': '3.0V to 5.5V, Low-Power, up to 1Mbps, True RS-232 Transceivers Using Four 0.1μF External Capacitors', 'kicadSymbolki_fp_filters': 'SOIC*P1.27mm* DIP*W7.62mm* TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Interface_UART : MAX3232')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

