
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG4005EJ"
    hexID = "SZKDIODEPMEG45EJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PMEG2005EJ', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG4005EJ', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-323F', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEGXX05EH_EJ_SER.pdf', 'kicadSymbolki_keywords': 'forward voltage diode', 'kicadSymbolki_description': '40V, 500mA very low Vf MEGA Schottky barrier rectifier, SOD-323F', 'kicadSymbolki_fp_filters': 'D*SOD?323F*'}])
    newPart['name'].append('PMEG4005EJ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

