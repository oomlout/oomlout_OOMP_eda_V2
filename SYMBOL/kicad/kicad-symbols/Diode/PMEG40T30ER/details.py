
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG40T30ER"
    hexID = "SZKDIODEPMEG4T3ER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PMEG40T10ER', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG40T30ER', 'kicadSymbolFootprint': 'Diode_SMD:Nexperia_CFP3_SOD-123W', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEG40T30ER.pdf', 'kicadSymbolki_keywords': 'forward voltage diode', 'kicadSymbolki_description': '40V, 3A low Vf Trench MEGA Schottky barrier rectifier, SOD-123W', 'kicadSymbolki_fp_filters': 'Nexperia*CFP3*SOD?123W*'}])
    newPart['name'].append('Diode : PMEG40T30ER')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

