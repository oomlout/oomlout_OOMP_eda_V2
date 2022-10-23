
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "ISO1050DUB"
    hexID = "SZKINTERFACECANLINISO15DUB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ISO1050DUB', 'kicadSymbolFootprint': 'Package_SO:SOP-8_6.62x9.15mm_P2.54mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/iso1050.pdf', 'kicadSymbolki_keywords': 'CAN Isolated', 'kicadSymbolki_description': 'Isolated CAN Transceiver, SOP-8', 'kicadSymbolki_fp_filters': 'SOP*6.62x9.15mm*P2.54mm*'}])
    newPart['name'].append('ISO1050DUB')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

