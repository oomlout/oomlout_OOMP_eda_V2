
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG060V050EPD"
    hexID = "SZKDIODEPMEG6V5EPD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PMEG45A10EPD', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG060V050EPD', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Nexperia_CFP15_SOT-1289', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEG060V050EPD.pdf', 'kicadSymbolki_keywords': 'forward voltage diode', 'kicadSymbolki_description': '60V, 5A low Vf MEGA Schottky barrier rectifier, SOT-1289', 'kicadSymbolki_fp_filters': 'Nexperia*CFP15*SOT?1289*'}])
    newPart['name'].append('PMEG060V050EPD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

