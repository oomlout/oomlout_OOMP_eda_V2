
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG3005EH"
    hexID = "SZKDIODEPMEG35EH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PMEG2005EH', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG3005EH', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-123F', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEGXX05EH_EJ_SER.pdf', 'kicadSymbolki_keywords': 'forward voltage diode', 'kicadSymbolki_description': '30V, 500mA very low Vf MEGA Schottky barrier rectifier, SOD-123F', 'kicadSymbolki_fp_filters': 'D*SOD?123F*'}])
    newPart['name'].append('Diode : PMEG3005EH')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

