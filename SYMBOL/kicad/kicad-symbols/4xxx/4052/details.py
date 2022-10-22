
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "4xxx"
    oIndex = "4052"
    hexID = "SZK4XXX452"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '4052', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/Intersil/documents/cd40/cd4051bms-52bms-53bms.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'CMOS MUX MUX4', 'kicadSymbolki_description': 'Dual Analog Multiplexer 4 to 1 line', 'kicadSymbolki_fp_filters': 'DIP?16*'}])
    newPart['name'].append('4052')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

