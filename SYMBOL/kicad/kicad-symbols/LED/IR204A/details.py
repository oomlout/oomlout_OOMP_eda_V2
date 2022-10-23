
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "IR204A"
    hexID = "SZKLIR24A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SFH4356P', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'IR204A', 'kicadSymbolFootprint': 'LED_THT:LED_D3.0mm_IRBlack', 'kicadSymbolDatasheet': 'http://www.everlight.com/file/ProductFile/IR204-A.pdf', 'kicadSymbolki_keywords': 'opto IR LED', 'kicadSymbolki_description': 'Infrared LED , 3mm LED package', 'kicadSymbolki_fp_filters': 'LED*3.0mm*IRBlack*'}])
    newPart['name'].append('IR204A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

