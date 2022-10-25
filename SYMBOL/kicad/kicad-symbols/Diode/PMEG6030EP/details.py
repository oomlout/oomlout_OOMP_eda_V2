
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG6030EP"
    hexID = "SZKDIODEPMEG63EP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PMEG4050EP', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG6030EP', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-128', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEG6030EP.pdf', 'kicadSymbolki_keywords': 'forward voltage diode', 'kicadSymbolki_description': '60V, 3A low Vf MEGA Schottky barrier rectifier, SOD-128', 'kicadSymbolki_fp_filters': 'D*SOD?128*'}])
    newPart['name'].append('Diode : PMEG6030EP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

