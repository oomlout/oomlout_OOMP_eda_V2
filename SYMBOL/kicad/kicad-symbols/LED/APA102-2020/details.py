
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "APA102-2020"
    hexID = "SZKLAPA1222"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'APA102-2020', 'kicadSymbolFootprint': 'LED_SMD:LED-APA102-2020', 'kicadSymbolDatasheet': 'http://www.led-color.com/upload/201604/APA102-2020%20SMD%20LED.pdf', 'kicadSymbolki_keywords': 'RGB LED addressable 8bit pwm 5bit greyscale', 'kicadSymbolki_description': 'RGB LED with integrated controller', 'kicadSymbolki_fp_filters': 'LED*APA102*'}])
    newPart['name'].append('APA102-2020')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

