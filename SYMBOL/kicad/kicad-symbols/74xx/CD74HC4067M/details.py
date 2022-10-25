
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "CD74HC4067M"
    hexID = "SZK74XXCD74HC467M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CD74HC4067M', 'kicadSymbolFootprint': 'Package_SO:SOIC-24W_7.5x15.4mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/cd74hc4067.pdf', 'kicadSymbolki_keywords': 'multiplexer demultiplexer mux demux', 'kicadSymbolki_description': 'High-Speed CMOS Logic 16-Channel Analog Multiplexer/Demultiplexer, SOIC-24', 'kicadSymbolki_fp_filters': 'SOIC*W*7.5x15.4mm*P1.27mm*'}])
    newPart['name'].append('74xx : CD74HC4067M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

