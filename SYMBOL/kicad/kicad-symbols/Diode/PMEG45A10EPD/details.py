
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG45A10EPD"
    hexID = "SZKDIODEPMEG45A1EPD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG45A10EPD', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Nexperia_CFP15_SOT-1289', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEG45A10EPD.pdf', 'kicadSymbolki_keywords': 'forward voltage diode', 'kicadSymbolki_description': '45V, 10A low Vf MEGA Schottky barrier rectifier, SOT-1289', 'kicadSymbolki_fp_filters': 'Nexperia*CFP15*SOT?1289*'}])
    newPart['name'].append('PMEG45A10EPD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

