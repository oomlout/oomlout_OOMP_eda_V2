
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "LT1080"
    hexID = "SZKINTERFACEUARTLT18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1080', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/10801fe.pdf', 'kicadSymbolki_keywords': 'rs232 uart transceiver', 'kicadSymbolki_description': 'Dual RS232 driver/receiver, 5V supply, 120kb/s', 'kicadSymbolki_fp_filters': 'SO* DIP*W7.62mm*'}])
    newPart['name'].append('Interface_UART : LT1080')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

