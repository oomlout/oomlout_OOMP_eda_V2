
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "SFH4550"
    hexID = "SZKLSFH455"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LD271', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SFH4550', 'kicadSymbolFootprint': 'LED_THT:LED_D5.0mm_IRGrey', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic3/00116140_0.pdf', 'kicadSymbolki_keywords': 'IR LED', 'kicadSymbolki_description': '950nm High-Power IR-LED, 5mm', 'kicadSymbolki_fp_filters': 'LED*5.0mm*IRGrey*'}])
    newPart['name'].append('SFH4550')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

