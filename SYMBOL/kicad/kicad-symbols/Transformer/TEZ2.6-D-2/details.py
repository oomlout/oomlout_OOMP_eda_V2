
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "TEZ2.6-D-2"
    hexID = "SZKTRTEZ26D2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'TEZ2.6-D-2', 'kicadSymbolFootprint': 'Transformer_THT:Transformer_Breve_TEZ-28x33', 'kicadSymbolDatasheet': 'http://www.breve.pl/pdf/ANG/TEZ_ang.pdf', 'kicadSymbolki_keywords': '2.6VA PCB Transformer Dual Secondary', 'kicadSymbolki_description': 'TEZ2.6/D/x-x, 2.6VA, Dual Secondary, Cast Resin Transformer, PCB', 'kicadSymbolki_fp_filters': 'Transformer*Breve*TEZ*28x33*'}])
    newPart['name'].append('TEZ2.6-D-2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

