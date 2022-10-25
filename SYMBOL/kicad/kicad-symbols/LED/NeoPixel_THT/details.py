
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "NeoPixel_THT"
    hexID = "SZKLNEOPIXELTHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'NeoPixel_THT', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.adafruit.com/product/1938', 'kicadSymbolki_keywords': 'RGB LED NeoPixel addressable', 'kicadSymbolki_description': 'RGB LED with integrated controller, 5mm/8mm LED package', 'kicadSymbolki_fp_filters': 'LED*D5.0mm* LED*D8.0mm*'}])
    newPart['name'].append('LED : NeoPixel_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

