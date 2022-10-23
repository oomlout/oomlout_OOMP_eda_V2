
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "PESD5V0L4UG"
    hexID = "SZKPOWERPROTECTIONPESD5VL4UG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PESD3V3L4UG', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PESD5V0L4UG', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PESDXL4UF_G_W.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Low capacitance unidirectional quadruple ESD protection diode array, 5.0V, Common Anode, SOT-353', 'kicadSymbolki_fp_filters': 'SOT?353*'}])
    newPart['name'].append('PESD5V0L4UG')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

