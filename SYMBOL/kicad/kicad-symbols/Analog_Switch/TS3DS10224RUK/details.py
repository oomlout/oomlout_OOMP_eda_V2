
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "TS3DS10224RUK"
    hexID = "SZKANALOGSWITCHTS3DS1224RUK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TS3DS10224RUK', 'kicadSymbolFootprint': 'Package_DFN_QFN:WQFN-20-1EP_3x3mm_P0.4mm_EP1.7x1.7mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ts3ds10224.pdf', 'kicadSymbolki_keywords': 'multiplexer demultiplexer 1:4 differential', 'kicadSymbolki_description': 'High-Speed Differential Crosspoint, WQFN-20', 'kicadSymbolki_fp_filters': 'WQFN*1EP*3x3mm*P0.4mm*'}])
    newPart['name'].append('TS3DS10224RUK')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

