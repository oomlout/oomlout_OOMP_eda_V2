
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BAT54J"
    hexID = "SZKDIODEBAT54J"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BAT54J', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-323F', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/BAT54J.pdf', 'kicadSymbolki_keywords': 'diode Schottky', 'kicadSymbolki_description': '30V 200mA Schottky diode, SOD-323F', 'kicadSymbolki_fp_filters': 'D*SOD?323F*'}])
    newPart['name'].append('Diode : BAT54J')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

