
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "ADM2582E"
    hexID = "SZKINTERFACEUARTADM2582E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADM2587E', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADM2582E', 'kicadSymbolFootprint': 'Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'www.analog.com/media/en/technical-documentation/data-sheets/ADM2582E_2587E.pdf', 'kicadSymbolki_keywords': 'RS485 Transceiver,RS422 Transceiver', 'kicadSymbolki_description': 'Isolated RS485/RS422 Transceiver,Integrated Isolated DC-DC Converter, 16Mbps,SO-20', 'kicadSymbolki_fp_filters': 'SOIC*7.5x12.8mm*P1.27mm*'}])
    newPart['name'].append('ADM2582E')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

