
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "DIN-5_180degree"
    hexID = "SZKCNDIN518DEGREE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'DIN-5_180degree', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.mouser.com/ds/2/18/40_c091_abd_e-75918.pdf', 'kicadSymbolki_keywords': 'circular DIN connector stereo audio', 'kicadSymbolki_description': '5-pin DIN connector (5-pin DIN-5 stereo)', 'kicadSymbolki_fp_filters': 'DIN*'}])
    newPart['name'].append('DIN-5_180degree')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

