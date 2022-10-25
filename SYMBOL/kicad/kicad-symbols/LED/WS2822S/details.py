
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "WS2822S"
    hexID = "SZKLWS2822S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'WS2822S', 'kicadSymbolFootprint': 'LED_SMD:LED_WS2812_PLCC6_5.0x5.0mm_P1.6mm', 'kicadSymbolDatasheet': 'http://akizukidenshi.com/download/ds/worldsemi/WS2822S.pdf', 'kicadSymbolki_keywords': 'RGB LED addressable', 'kicadSymbolki_description': 'RGB LED with integrated controller', 'kicadSymbolki_fp_filters': 'LED*WS2812*PLCC*5.0x5.0mm*P1.6mm*'}])
    newPart['name'].append('LED : WS2822S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

