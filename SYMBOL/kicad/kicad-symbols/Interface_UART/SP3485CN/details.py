
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "SP3485CN"
    hexID = "SZKINTERFACEUARTSP3485CN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SP3481CN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SP3485CN', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.icbase.com/pdf/SPX/SPX00480106.pdf', 'kicadSymbolki_keywords': 'Low Power Half-Duplex RS-485 Transceiver 10Mbps', 'kicadSymbolki_description': '3.3V Low Power Half-Duplex RS-485 Transceiver 10Mbps, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Interface_UART : SP3485CN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

