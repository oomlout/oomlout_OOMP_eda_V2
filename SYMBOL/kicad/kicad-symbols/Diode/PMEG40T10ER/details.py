
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG40T10ER"
    hexID = "SZKDIODEPMEG4T1ER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG40T10ER', 'kicadSymbolFootprint': 'Diode_SMD:Nexperia_CFP3_SOD-123W', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEG40T10ER.pdf', 'kicadSymbolki_keywords': 'forward voltage diode', 'kicadSymbolki_description': '40V, 1A low Vf Trench MEGA Schottky barrier rectifier, SOD-123W', 'kicadSymbolki_fp_filters': 'Nexperia*CFP3*SOD?123W*'}])
    newPart['name'].append('PMEG40T10ER')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

