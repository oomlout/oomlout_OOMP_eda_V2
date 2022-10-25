
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "LTC2861"
    hexID = "SZKINTERFACEUARTLTC2861"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC2861', 'kicadSymbolFootprint': 'Package_SO:SSOP-28_5.3x10.2mm_P0.65mm', 'kicadSymbolDatasheet': 'linear-tecltc2859-2861.pdf', 'kicadSymbolki_keywords': 'RS485', 'kicadSymbolki_description': '20Mbps RS485 transceiver with tntegrated switchable termination', 'kicadSymbolki_fp_filters': 'SSOP*'}])
    newPart['name'].append('Interface_UART : LTC2861')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

