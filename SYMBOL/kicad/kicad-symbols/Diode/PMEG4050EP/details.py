
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG4050EP"
    hexID = "SZKDIODEPMEG45EP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG4050EP', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-128', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEG4050EP.pdf', 'kicadSymbolki_keywords': 'forward voltage diode', 'kicadSymbolki_description': '40V, 5A low Vf Schottky barrier rectifier, SOD-128', 'kicadSymbolki_fp_filters': 'D*SOD?128*'}])
    newPart['name'].append('Diode : PMEG4050EP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

