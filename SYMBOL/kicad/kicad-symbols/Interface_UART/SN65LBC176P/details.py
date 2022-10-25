
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "SN65LBC176P"
    hexID = "SZKINTERFACEUARTSN65LBC176P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SN75LBC176P', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SN65LBC176P', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn75lbc176.pdf', 'kicadSymbolki_keywords': 'Differential bus transceiver', 'kicadSymbolki_description': 'Differential bus transceiver, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Interface_UART : SN65LBC176P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

