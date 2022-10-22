
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS165"
    hexID = "SZK74XX74LS165"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS165', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/sn74ls165a.pdf', 'kicadSymbolki_keywords': 'TTL SR SR8', 'kicadSymbolki_description': 'Shift Register 8-bit, parallel load', 'kicadSymbolki_fp_filters': 'DIP?16* SO*16*3.9x9.9mm*P1.27mm* SSOP*16*5.3x6.2mm*P0.65mm* TSSOP*16*4.4x5mm*P0.65*'}])
    newPart['name'].append('74LS165')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

