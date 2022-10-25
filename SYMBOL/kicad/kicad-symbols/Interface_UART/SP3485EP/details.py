
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "SP3485EP"
    hexID = "SZKINTERFACEUARTSP3485EP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SP3481CP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SP3485EP', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://www.icbase.com/pdf/SPX/SPX00480106.pdf', 'kicadSymbolki_keywords': 'Low Power Half-Duplex RS-485 Transceiver 10Mbps', 'kicadSymbolki_description': 'Industrial 3.3V Low Power Half-Duplex RS-485 Transceiver 10Mbps, DIP8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Interface_UART : SP3485EP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

