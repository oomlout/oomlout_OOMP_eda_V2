
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG60T20ELR"
    hexID = "SZKDIODEPMEG6T2ELR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PMEG40T10ER', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG60T20ELR', 'kicadSymbolFootprint': 'Diode_SMD:Nexperia_CFP3_SOD-123W', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEG60T20ELR.pdf', 'kicadSymbolki_keywords': 'ir diode', 'kicadSymbolki_description': '60V, 2A low leakage current Trench MEGA Schottky barrier rectifier, SOD-123W', 'kicadSymbolki_fp_filters': 'Nexperia*CFP3*SOD?123W*'}])
    newPart['name'].append('PMEG60T20ELR')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

