
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "1N5404"
    hexID = "SZKDIODE1N544"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '1N4001', 'kicadSymbolReference': 'D', 'kicadSymbolValue': '1N5404', 'kicadSymbolFootprint': 'Diode_THT:D_DO-201AD_P15.24mm_Horizontal', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/88516/1n5400.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '400V 3A General Purpose Rectifier Diode, DO-201AD', 'kicadSymbolki_fp_filters': 'D*DO?201AD*'}])
    newPart['name'].append('Diode : 1N5404')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

