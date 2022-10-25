
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "TEZ16.0-D-2"
    hexID = "SZKTRTEZ16D2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'TEZ16.0-D-2', 'kicadSymbolFootprint': 'Transformer_THT:Transformer_Breve_TEZ-47x57', 'kicadSymbolDatasheet': 'http://www.breve.pl/pdf/ANG/TEZ_ang.pdf', 'kicadSymbolki_keywords': '16VA PCB Transformer Dual Secondary', 'kicadSymbolki_description': 'TEZ16.0/D/x-x, 16VA, Dual Secondary, Cast Resin Transformer, PCB', 'kicadSymbolki_fp_filters': 'Transformer*Breve*TEZ*47x57*'}])
    newPart['name'].append('Transformer : TEZ16.0-D-2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

