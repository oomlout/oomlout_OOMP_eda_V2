
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "SN65LBC176QD"
    hexID = "SZKINTERFACEUARTSN65LBC176QD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SN75LBC176D', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SN65LBC176QD', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn75lbc176.pdf', 'kicadSymbolki_keywords': 'Differential bus transceiver', 'kicadSymbolki_description': 'Differential bus transceiver, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Interface_UART : SN65LBC176QD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

