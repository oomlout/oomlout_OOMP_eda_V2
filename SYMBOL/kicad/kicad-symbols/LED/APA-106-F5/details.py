
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "APA-106-F5"
    hexID = "SZKLAPA16F5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'APA-106-F5', 'kicadSymbolFootprint': 'LED_THT:LED_D5.0mm-4_RGB', 'kicadSymbolDatasheet': 'https://cdn.sparkfun.com/datasheets/Components/LED/COM-12877.pdf', 'kicadSymbolki_keywords': 'RGB LED addressable 8bit pwm 5bit greyscale', 'kicadSymbolki_description': 'RGB LED with integrated controller, 5mm Package', 'kicadSymbolki_fp_filters': 'LED*D5.0mm*RGB*'}])
    newPart['name'].append('APA-106-F5')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

