
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "PESD3V3L4UF"
    hexID = "SZKPOWERPROTECTIONPESD3V3L4UF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PESD3V3L4UF', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-886', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PESDXL4UF_G_W.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Low capacitance unidirectional quadruple ESD protection diode array, 3.3V, Common Anode, SOT-886', 'kicadSymbolki_fp_filters': 'SOT?886*'}])
    newPart['name'].append('PESD3V3L4UF')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

