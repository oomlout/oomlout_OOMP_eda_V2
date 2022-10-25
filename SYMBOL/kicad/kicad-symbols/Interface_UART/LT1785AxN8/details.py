
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "LT1785AxN8"
    hexID = "SZKINTERFACEUARTLT1785AXN8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1785xN8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1785AxN8', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/LT1785-1785A-1791-1791A.pdf', 'kicadSymbolki_keywords': 'RS485 RS422 transceiver half duplex', 'kicadSymbolki_description': 'RS-485, RS-422 Half duplex 250kbps transceiver, fail-safe receiver, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Interface_UART : LT1785AxN8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

