
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "1N5821"
    hexID = "SZKDIODE1N5821"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '1N5820', 'kicadSymbolReference': 'D', 'kicadSymbolValue': '1N5821', 'kicadSymbolFootprint': 'Diode_THT:D_DO-201AD_P15.24mm_Horizontal', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/88526/1n5820.pdf', 'kicadSymbolki_keywords': 'diode Schottky', 'kicadSymbolki_description': '30V 3A Schottky Barrier Rectifier Diode, DO-201AD', 'kicadSymbolki_fp_filters': 'D*DO?201AD*'}])
    newPart['name'].append('Diode : 1N5821')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

