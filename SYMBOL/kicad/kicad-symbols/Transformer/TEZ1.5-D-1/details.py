
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "TEZ1.5-D-1"
    hexID = "SZKTRTEZ15D1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'TEZ1.5-D-1', 'kicadSymbolFootprint': 'Transformer_THT:Transformer_Breve_TEZ-28x33', 'kicadSymbolDatasheet': 'http://www.breve.pl/pdf/ANG/TEZ_ang.pdf', 'kicadSymbolki_keywords': '1.5VA PCB Transformer Single Secondary', 'kicadSymbolki_description': 'TEZ1.5/D/x, 1.5VA, Single Secondary, Cast Resin Transformer, PCB', 'kicadSymbolki_fp_filters': 'Transformer*Breve*TEZ*28x33*'}])
    newPart['name'].append('Transformer : TEZ1.5-D-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

