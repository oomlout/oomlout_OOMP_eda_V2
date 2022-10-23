
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "TPIC6595"
    hexID = "SZKINTERFACEEXPANSIONTPIC6595"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPIC6595', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tpic6595.pdf', 'kicadSymbolki_keywords': 'shift register 8bit', 'kicadSymbolki_description': 'Power Logic 8-bit Shift Register, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*7.5x12.8mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('TPIC6595')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

