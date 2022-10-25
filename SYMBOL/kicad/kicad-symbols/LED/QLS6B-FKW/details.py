
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "QLS6B-FKW"
    hexID = "SZKLQLS6BFKW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CLS6B-FKW', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'QLS6B-FKW', 'kicadSymbolFootprint': 'LED_SMD:LED_Cree-PLCC6_4.7x1.5mm', 'kicadSymbolDatasheet': 'https://www.cree.com/led-components/media/documents/1397-QLS6BFKW.pdf', 'kicadSymbolki_keywords': 'LED RGB', 'kicadSymbolki_description': 'Cree PLCC6 3 in 1 SMD LED, PLCC-6', 'kicadSymbolki_fp_filters': 'LED*Cree*PLCC*4.7x1.5mm*'}])
    newPart['name'].append('LED : QLS6B-FKW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

