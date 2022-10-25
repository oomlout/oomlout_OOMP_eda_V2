
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG3010CEJ"
    hexID = "SZKDIODEPMEG31CEJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PMEG2005EJ', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG3010CEJ', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-323F', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEG3010CEH_PMEG3010CEJ.pdf', 'kicadSymbolki_keywords': 'forward voltage diode', 'kicadSymbolki_description': '30V, 1A very low Vf MEGA Schottky barrier rectifier, SOD-323F', 'kicadSymbolki_fp_filters': 'D*SOD?323F*'}])
    newPart['name'].append('Diode : PMEG3010CEJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

