
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "SK6812MINI"
    hexID = "SZKLSK6812M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SK6812MINI', 'kicadSymbolFootprint': 'LED_SMD:LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm', 'kicadSymbolDatasheet': 'https://cdn-shop.adafruit.com/product-files/2686/SK6812MINI_REV.01-1-2.pdf', 'kicadSymbolki_keywords': 'RGB LED NeoPixel Mini addressable', 'kicadSymbolki_description': 'RGB LED with integrated controller', 'kicadSymbolki_fp_filters': 'LED*SK6812MINI*PLCC*3.5x3.5mm*P1.75mm*'}])
    newPart['name'].append('LED : SK6812MINI')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

