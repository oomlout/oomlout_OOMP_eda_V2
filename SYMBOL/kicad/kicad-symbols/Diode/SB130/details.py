
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "SB130"
    hexID = "SZKDIODESB13"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SB120', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SB130', 'kicadSymbolFootprint': 'Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal', 'kicadSymbolDatasheet': 'http://www.diodes.com/_files/datasheets/ds23022.pdf', 'kicadSymbolki_keywords': 'diode Schottky', 'kicadSymbolki_description': '30V 1A Schottky Barrier Rectifier Diode, DO-41', 'kicadSymbolki_fp_filters': 'D*DO?41*'}])
    newPart['name'].append('Diode : SB130')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

