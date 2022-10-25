
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "PMEG4010ET"
    hexID = "SZKDIODEPMEG41ET"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PMEG2010AET', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PMEG4010ET', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMEG4010EH_EJ_ET.pdf', 'kicadSymbolki_keywords': 'forward voltage diode', 'kicadSymbolki_description': '40V, 1A very low Vf MEGA Schottky barrier rectifier, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Diode : PMEG4010ET')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

