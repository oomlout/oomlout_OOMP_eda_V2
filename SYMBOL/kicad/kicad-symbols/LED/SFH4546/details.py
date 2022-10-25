
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "SFH4546"
    hexID = "SZKLSFH4546"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LD271', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SFH4546', 'kicadSymbolFootprint': 'LED_THT:LED_D5.0mm_IRGrey', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic1/00101982_0.pdf', 'kicadSymbolki_keywords': 'IR LED', 'kicadSymbolki_description': 'High-Power IR LED 940nm', 'kicadSymbolki_fp_filters': 'LED*5.0mm*IRGrey*'}])
    newPart['name'].append('LED : SFH4546')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

