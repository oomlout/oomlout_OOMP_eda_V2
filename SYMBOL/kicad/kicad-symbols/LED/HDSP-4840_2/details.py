
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "HDSP-4840_2"
    hexID = "SZKLHDSP4842"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'BAR', 'kicadSymbolValue': 'HDSP-4840_2', 'kicadSymbolFootprint': 'Display:HDSP-4840', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-1798EN', 'kicadSymbolki_keywords': 'display LED array', 'kicadSymbolki_description': 'BAR GRAPH 10 segment block, yellow', 'kicadSymbolki_fp_filters': 'HDSP?48*'}])
    newPart['name'].append('LED : HDSP-4840_2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

