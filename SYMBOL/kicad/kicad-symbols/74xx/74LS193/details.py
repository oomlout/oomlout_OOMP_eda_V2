
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS193"
    hexID = "SZK74XX74LS193"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LS192', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS193', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn74ls193.pdf', 'kicadSymbolki_keywords': 'TTL CNT CNT4', 'kicadSymbolki_description': 'Synchronous 4-bit Up/Down (2 clk) counter', 'kicadSymbolki_fp_filters': 'SOIC*3.9x9.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('74LS193')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

