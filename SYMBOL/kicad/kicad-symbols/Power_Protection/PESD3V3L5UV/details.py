
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "PESD3V3L5UV"
    hexID = "SZKPOWERPROTECTIONPESD3V3L5UV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PESD3V3L5UV', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-666', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PESDXL5UF_V_Y.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Low capacitance unidirectional fivefold ESD protection diode array, 3.3V, Common Anode, SOT-666', 'kicadSymbolki_fp_filters': 'SOT?666*'}])
    newPart['name'].append('Power_Protection : PESD3V3L5UV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

