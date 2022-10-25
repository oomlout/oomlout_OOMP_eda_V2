
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG10010ELR"
    hexID = "SZKDIODEPMEG11ELR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PMEG40T10ER', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG10010ELR', 'kicadSymbolFootprint': 'Diode_SMD:Nexperia_CFP3_SOD-123W', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEG10010ELR.pdf', 'kicadSymbolki_keywords': 'ir diode', 'kicadSymbolki_description': '100V, 1A low leakage current MEGA Schottky barrier rectifier, SOD-123W', 'kicadSymbolki_fp_filters': 'Nexperia*CFP3*SOD?123W*'}])
    newPart['name'].append('Diode : PMEG10010ELR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

