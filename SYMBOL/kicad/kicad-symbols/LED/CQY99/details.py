
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "CQY99"
    hexID = "SZKLCQY99"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LD271', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'CQY99', 'kicadSymbolFootprint': 'LED_THT:LED_D5.0mm_IRGrey', 'kicadSymbolDatasheet': 'https://www.prtice.info/IMG/pdf/CQY99.pdf', 'kicadSymbolki_keywords': 'IR LED', 'kicadSymbolki_description': '950nm IR-LED, 5mm', 'kicadSymbolki_fp_filters': 'LED*5.0mm*IRGrey*'}])
    newPart['name'].append('LED : CQY99')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

