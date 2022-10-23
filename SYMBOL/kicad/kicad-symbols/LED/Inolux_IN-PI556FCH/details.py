
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "Inolux_IN-PI556FCH"
    hexID = "SZKLINOLUXINPI556FCH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'Inolux_IN-PI556FCH', 'kicadSymbolFootprint': 'LED_SMD:LED_WS2812_PLCC6_5.0x5.0mm_P1.6mm', 'kicadSymbolDatasheet': 'http://www.inolux-corp.com/datasheet/SMDLED/Addressable%20LED/IN-PI556FCH.pdf', 'kicadSymbolki_keywords': 'RGB LED NeoPixel addressable', 'kicadSymbolki_description': '5050 RGB LED 6-Pin with integrated IC', 'kicadSymbolki_fp_filters': 'LED*WS2812*PLCC*5.0x5.0mm*P1.6mm*'}])
    newPart['name'].append('Inolux_IN-PI556FCH')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

