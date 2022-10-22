
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG3010ER"
    hexID = "SZKDIODEPMEG31ER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PMEG40T10ER', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG3010ER', 'kicadSymbolFootprint': 'Diode_SMD:Nexperia_CFP3_SOD-123W', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEG3010ER.pdf', 'kicadSymbolki_keywords': 'forward voltage diode', 'kicadSymbolki_description': '30V, 1A low Vf MEGA Schottky barrier rectifier, SOD-123W', 'kicadSymbolki_fp_filters': 'Nexperia*CFP3*SOD?123W*'}])
    newPart['name'].append('PMEG3010ER')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

