
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "IR26-21C_L110_TR8"
    hexID = "SZKLIR2621CL11TR8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'IR26-21C_L110_TR8', 'kicadSymbolFootprint': 'LED_SMD:LED_1206_3216Metric', 'kicadSymbolDatasheet': 'http://www.everlight.com/file/ProductFile/IR26-21C-L110-TR8.pdf', 'kicadSymbolki_keywords': 'IR LED', 'kicadSymbolki_description': '940nm, 20 deg, Infrared LED, 1206', 'kicadSymbolki_fp_filters': 'LED*1206*3216Metric*'}])
    newPart['name'].append('IR26-21C_L110_TR8')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

