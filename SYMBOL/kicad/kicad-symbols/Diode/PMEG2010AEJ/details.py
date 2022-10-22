
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG2010AEJ"
    hexID = "SZKDIODEPMEG21AEJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PMEG2005EJ', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG2010AEJ', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-323F', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEG2010AEJ.pdf', 'kicadSymbolki_keywords': 'forward voltage diode', 'kicadSymbolki_description': '20V, 1A very low Vf MEGA Schottky barrier rectifier, SOD-323F', 'kicadSymbolki_fp_filters': 'D*SOD?323F*'}])
    newPart['name'].append('PMEG2010AEJ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

