
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "HDSP-4832"
    hexID = "SZKLHDSP4832"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'BAR', 'kicadSymbolValue': 'HDSP-4832', 'kicadSymbolFootprint': 'Display:HDSP-4832', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-1798EN', 'kicadSymbolki_keywords': 'display LED array', 'kicadSymbolki_description': '10-element LED arrays, Mix of high efficient red, yellow and green', 'kicadSymbolki_fp_filters': 'HDSP?48*'}])
    newPart['name'].append('LED : HDSP-4832')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

