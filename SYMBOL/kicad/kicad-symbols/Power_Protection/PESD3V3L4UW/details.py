
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "PESD3V3L4UW"
    hexID = "SZKPOWERPROTECTIONPESD3V3L4UW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PESD3V3L4UW', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-665', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PESDXL4UF_G_W.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Low capacitance unidirectional quadruple ESD protection diode array, 3.3V, Common Anode, SOT-665', 'kicadSymbolki_fp_filters': 'SOT?665*'}])
    newPart['name'].append('Power_Protection : PESD3V3L4UW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

