
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74CBTLV3257"
    hexID = "SZK74XX74CBTLV3257"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74CBTLV3257', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn74cbtlv3257.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'mux demux low-voltage', 'kicadSymbolki_description': 'Quad 1:2 FET Multiplexer/Demultiplexer, Low-Voltage', 'kicadSymbolki_fp_filters': 'SSOP*3.9x4.9mm*P0.635mm* TSSOP*4.4x5mm*P0.65mm* TVSOP*4.4x3.6mm*P0.4mm* SOIC*3.9x9.9mm*P1.27mm*'}])
    newPart['name'].append('74CBTLV3257')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

