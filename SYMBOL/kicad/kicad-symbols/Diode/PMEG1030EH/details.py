
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG1030EH"
    hexID = "SZKDIODEPMEG13EH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PMEG2005EH', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG1030EH', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-123F', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEG1030EH_EJ.pdf', 'kicadSymbolki_keywords': 'forward voltage diode', 'kicadSymbolki_description': '10V, 3A ultra low Vf MEGA Schottky barrier rectifier, SOD-123F', 'kicadSymbolki_fp_filters': 'D*SOD?123F*'}])
    newPart['name'].append('PMEG1030EH')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

