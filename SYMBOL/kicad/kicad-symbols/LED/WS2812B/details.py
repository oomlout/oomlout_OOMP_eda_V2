
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "WS2812B"
    hexID = "SZKLWS2812B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'WS2812B', 'kicadSymbolFootprint': 'LED_SMD:LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm', 'kicadSymbolDatasheet': 'https://cdn-shop.adafruit.com/datasheets/WS2812B.pdf', 'kicadSymbolki_keywords': 'RGB LED NeoPixel addressable', 'kicadSymbolki_description': 'RGB LED with integrated controller', 'kicadSymbolki_fp_filters': 'LED*WS2812*PLCC*5.0x5.0mm*P3.2mm*'}])
    newPart['name'].append('WS2812B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

