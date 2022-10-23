
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "WS2812S"
    hexID = "SZKLWS2812S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'WS2812S', 'kicadSymbolFootprint': 'LED_SMD:LED_WS2812_PLCC6_5.0x5.0mm_P1.6mm', 'kicadSymbolDatasheet': 'http://www.world-semi.com/DownLoadFile/115', 'kicadSymbolki_keywords': 'RGB LED addressable', 'kicadSymbolki_description': 'RGB LED with integrated controller', 'kicadSymbolki_fp_filters': 'LED*WS2812*PLCC*5.0x5.0mm*P1.6mm*'}])
    newPart['name'].append('WS2812S')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

