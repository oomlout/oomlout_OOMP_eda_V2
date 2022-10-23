
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "WS2812"
    hexID = "SZKLWS2812"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'WS2812S', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'WS2812', 'kicadSymbolFootprint': 'LED_SMD:LED_WS2812_PLCC6_5.0x5.0mm_P1.6mm', 'kicadSymbolDatasheet': 'https://cdn-shop.adafruit.com/datasheets/WS2812.pdf', 'kicadSymbolki_keywords': 'RGB LED NeoPixel addressable', 'kicadSymbolki_description': 'RGB LED with integrated controller', 'kicadSymbolki_fp_filters': 'LED*WS2812*PLCC*5.0x5.0mm*P1.6mm*'}])
    newPart['name'].append('WS2812')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

