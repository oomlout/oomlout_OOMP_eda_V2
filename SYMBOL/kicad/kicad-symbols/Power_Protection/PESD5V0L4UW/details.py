
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "PESD5V0L4UW"
    hexID = "SZKPOWERPROTECTIONPESD5VL4UW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PESD3V3L4UW', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PESD5V0L4UW', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-665', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PESDXL4UF_G_W.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Low capacitance unidirectional quadruple ESD protection diode array, 5.0V, Common Anode, SOT-665', 'kicadSymbolki_fp_filters': 'SOT?665*'}])
    newPart['name'].append('PESD5V0L4UW')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

