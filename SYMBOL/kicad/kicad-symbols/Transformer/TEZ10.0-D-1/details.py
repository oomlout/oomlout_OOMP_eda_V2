
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "TEZ10.0-D-1"
    hexID = "SZKTRTEZ1D1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'TEZ10.0-D-1', 'kicadSymbolFootprint': 'Transformer_THT:Transformer_Breve_TEZ-44x52', 'kicadSymbolDatasheet': 'http://www.breve.pl/pdf/ANG/TEZ_ang.pdf', 'kicadSymbolki_keywords': '10VA PCB Transformer Single Secondary', 'kicadSymbolki_description': 'TEZ10.0/D/x, 10VA, Single Secondary, Cast Resin Transformer, PCB', 'kicadSymbolki_fp_filters': 'Transformer*Breve*TEZ*44x52*'}])
    newPart['name'].append('TEZ10.0-D-1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

