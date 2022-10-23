
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "GD75232DB"
    hexID = "SZKINTERFACEUARTGD75232DB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'GD65232DB', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'GD75232DB', 'kicadSymbolFootprint': 'Package_SO:SSOP-20_4.4x6.5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/gd75232.pdf', 'kicadSymbolki_keywords': 'RS232 UART Driver Receiver Interface', 'kicadSymbolki_description': 'Multiple RS-232 Driver and Receiver, SSOP-20', 'kicadSymbolki_fp_filters': 'SSOP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('GD75232DB')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

