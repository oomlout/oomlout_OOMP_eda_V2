
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "PESD5V0L4UF"
    hexID = "SZKPOWERPROTECTIONPESD5VL4UF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PESD3V3L4UF', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PESD5V0L4UF', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-886', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PESDXL4UF_G_W.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Low capacitance unidirectional quadruple ESD protection diode array, 5.0V, Common Anode, SOT-886', 'kicadSymbolki_fp_filters': 'SOT?886*'}])
    newPart['name'].append('Power_Protection : PESD5V0L4UF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

