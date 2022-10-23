
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "PESD5V0L5UV"
    hexID = "SZKPOWERPROTECTIONPESD5VL5UV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PESD3V3L5UV', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PESD5V0L5UV', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-666', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PESDXL5UF_V_Y.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Low capacitance unidirectional fivefold ESD protection diode array, 5.0V, Common Anode, SOT-666', 'kicadSymbolki_fp_filters': 'SOT?666*'}])
    newPart['name'].append('PESD5V0L5UV')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

