
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "1N5819"
    hexID = "SZKDIODE1N5819"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SB120', 'kicadSymbolReference': 'D', 'kicadSymbolValue': '1N5819', 'kicadSymbolFootprint': 'Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/88525/1n5817.pdf', 'kicadSymbolki_keywords': 'diode Schottky', 'kicadSymbolki_description': '40V 1A Schottky Barrier Rectifier Diode, DO-41', 'kicadSymbolki_fp_filters': 'D*DO?41*'}])
    newPart['name'].append('Diode : 1N5819')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

