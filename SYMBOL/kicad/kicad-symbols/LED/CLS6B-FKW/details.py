
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "CLS6B-FKW"
    hexID = "SZKLCLS6BFKW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'CLS6B-FKW', 'kicadSymbolFootprint': 'LED_SMD:LED_Cree-PLCC6_4.7x1.5mm', 'kicadSymbolDatasheet': 'https://www.cree.com/led-components/media/documents/CLS6B-FKW.pdf', 'kicadSymbolki_keywords': 'LED RGB', 'kicadSymbolki_description': 'Cree PLCC6 3 in 1 SMD LED, PLCC-6', 'kicadSymbolki_fp_filters': 'LED*Cree*PLCC*4.7x1.5mm*'}])
    newPart['name'].append('CLS6B-FKW')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

