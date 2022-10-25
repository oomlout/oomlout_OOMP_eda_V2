
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "B130-E3"
    hexID = "SZKDIODEB13E3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'B120-E3', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'B130-E3', 'kicadSymbolFootprint': 'Diode_SMD:D_SMA', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/88946/b120.pdf', 'kicadSymbolki_keywords': 'diode Schottky', 'kicadSymbolki_description': '30V 1A Schottky Barrier Rectifier Diode, SMA(DO-214AC)', 'kicadSymbolki_fp_filters': 'D*SMA*'}])
    newPart['name'].append('Diode : B130-E3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

