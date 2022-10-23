
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "NSL-32"
    hexID = "SZKISOLATORNSL32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NSL-32', 'kicadSymbolFootprint': 'OptoDevice:Luna_NSL-32', 'kicadSymbolDatasheet': 'http://lunainc.com/wp-content/uploads/2016/06/NSL-32.pdf', 'kicadSymbolki_keywords': 'optocoupler', 'kicadSymbolki_description': 'Optocoupler, LED Input, Photocell Output', 'kicadSymbolki_fp_filters': 'Luna*NSL?32*'}])
    newPart['name'].append('NSL-32')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

