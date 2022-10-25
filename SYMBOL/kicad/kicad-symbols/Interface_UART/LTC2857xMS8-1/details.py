
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "LTC2857xMS8-1"
    hexID = "SZKINTERFACEUARTLTC2857XMS81"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC2851xMS8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC2857xMS8-1', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/285678fg.pdf', 'kicadSymbolki_keywords': 'RS485 RS422 transceiver full duplex', 'kicadSymbolki_description': 'RS-485, RS-422 Full duplex 20Mbps transceiver, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Interface_UART : LTC2857xMS8-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

