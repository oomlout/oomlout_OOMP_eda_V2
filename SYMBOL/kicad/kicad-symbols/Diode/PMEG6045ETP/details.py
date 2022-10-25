
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG6045ETP"
    hexID = "SZKDIODEPMEG645ETP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PMEG4050EP', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG6045ETP', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-128', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEG6045ETP.pdf', 'kicadSymbolki_keywords': 'forward voltage diode', 'kicadSymbolki_description': '60V, 4.5A High-Temperature Schottky barrier rectifier, SOD-128', 'kicadSymbolki_fp_filters': 'D*SOD?128*'}])
    newPart['name'].append('Diode : PMEG6045ETP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

