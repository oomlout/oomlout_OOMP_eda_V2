
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "CD74HC4067SM"
    hexID = "SZK74XXCD74HC467SM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CD74HC4067SM', 'kicadSymbolFootprint': 'Package_SO:SSOP-24_5.3x8.2mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/cd74hc4067.pdf', 'kicadSymbolki_keywords': 'multiplexer demultiplexer mux demux', 'kicadSymbolki_description': 'High-Speed CMOS Logic 16-Channel Analog Multiplexer/Demultiplexer, SSOP-24', 'kicadSymbolki_fp_filters': 'SSOP*5.3x8.2mm*P0.65mm*'}])
    newPart['name'].append('CD74HC4067SM')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

