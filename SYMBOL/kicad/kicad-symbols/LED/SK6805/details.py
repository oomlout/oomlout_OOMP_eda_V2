
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "SK6805"
    hexID = "SZKLSK685"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SK6805', 'kicadSymbolFootprint': 'LED_SMD:LED_SK6805_PLCC4_2.4x2.7mm_P1.3mm', 'kicadSymbolDatasheet': 'https://cdn-shop.adafruit.com/product-files/3484/3484_Datasheet.pdf', 'kicadSymbolki_keywords': 'RGB LED NeoPixel Nano addressable', 'kicadSymbolki_description': 'RGB LED with integrated controller', 'kicadSymbolki_fp_filters': 'LED*SK6805*PLCC*2.4x2.7mm*P1.3mm*'}])
    newPart['name'].append('LED : SK6805')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

