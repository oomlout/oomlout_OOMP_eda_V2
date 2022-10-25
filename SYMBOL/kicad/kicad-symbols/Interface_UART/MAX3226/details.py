
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "MAX3226"
    hexID = "SZKINTERFACEUARTMAX3226"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX3226', 'kicadSymbolFootprint': 'Package_SO:SSOP-16_5.3x6.2mm_P0.65mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX3224-MAX3245.pdf', 'kicadSymbolki_keywords': 'rs232 uart transceiver', 'kicadSymbolki_description': 'Single RS232 driver/receiver, 3.0V to 5V supply, 250kb/s, AutoShutdown Plus, SSOP-16 package', 'kicadSymbolki_fp_filters': 'SSOP*5.3x6.2mm*P0.65mm*'}])
    newPart['name'].append('Interface_UART : MAX3226')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

