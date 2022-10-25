
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "CLV1L-FKB"
    hexID = "SZKLCLV1LFKB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'CLV1L-FKB', 'kicadSymbolFootprint': 'LED_SMD:LED_Cree-PLCC4_3.2x2.8mm_CCW', 'kicadSymbolDatasheet': 'http://www.cree.com/led-components/media/documents/CLV1L-FKB-1238.pdf', 'kicadSymbolki_keywords': 'led rgb diode', 'kicadSymbolki_description': 'Cree PLCC4 3 in 1 SMD LED', 'kicadSymbolki_fp_filters': '*Cree*PLCC4*3.2x2.8mm*'}])
    newPart['name'].append('LED : CLV1L-FKB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

