
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG2020EH"
    hexID = "SZKDIODEPMEG22EH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PMEG2005EH', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG2020EH', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-123F', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEG2020EH_EJ.pdf', 'kicadSymbolki_keywords': 'forward voltage diode', 'kicadSymbolki_description': '20V, 2A very low Vf MEGA Schottky barrier rectifier, SOD-123F', 'kicadSymbolki_fp_filters': 'D*SOD?123F*'}])
    newPart['name'].append('Diode : PMEG2020EH')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

