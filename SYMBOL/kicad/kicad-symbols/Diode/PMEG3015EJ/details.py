
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG3015EJ"
    hexID = "SZKDIODEPMEG315EJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PMEG2005EJ', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG3015EJ', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-323F', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEG3015EH_EJ.pdf', 'kicadSymbolki_keywords': 'forward voltage diode', 'kicadSymbolki_description': '30V, 1.5A ultra low Vf MEGA Schottky barrier rectifier, SOD-323F', 'kicadSymbolki_fp_filters': 'D*SOD?323F*'}])
    newPart['name'].append('PMEG3015EJ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

