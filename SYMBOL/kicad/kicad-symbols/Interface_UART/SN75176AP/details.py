
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "SN75176AP"
    hexID = "SZKINTERFACEUARTSN75176AP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SN75LBC176P', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SN75176AP', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn75176a.pdf', 'kicadSymbolki_keywords': 'Differential bus transceiver', 'kicadSymbolki_description': 'Differential RS-422/RS-485 bus transceiver, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Interface_UART : SN75176AP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

