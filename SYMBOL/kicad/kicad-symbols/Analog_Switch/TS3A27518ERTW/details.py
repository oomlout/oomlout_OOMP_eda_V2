
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "TS3A27518ERTW"
    hexID = "SZKANALOGSWITCHTS3A27518ERTW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TS3A27518ERTW', 'kicadSymbolFootprint': 'Package_DFN_QFN:WQFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ts3a27518e.pdf', 'kicadSymbolki_keywords': 'SPI qSPI multiplexer demux', 'kicadSymbolki_description': '6-channel analog mux, WQFN-24', 'kicadSymbolki_fp_filters': 'WQFN*4x4mm*P0.5mm*'}])
    newPart['name'].append('TS3A27518ERTW')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

