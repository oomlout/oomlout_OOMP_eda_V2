
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "GD75232DW"
    hexID = "SZKINTERFACEUARTGD75232DW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'GD65232DW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'GD75232DW', 'kicadSymbolFootprint': 'Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/gd75232.pdf', 'kicadSymbolki_keywords': 'RS232 UART Driver Receiver Interface', 'kicadSymbolki_description': 'Multiple RS-232 Driver and Receiver, SOIC-20', 'kicadSymbolki_fp_filters': 'SOIC*7.5x12.8mm*P1.27mm*'}])
    newPart['name'].append('Interface_UART : GD75232DW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

