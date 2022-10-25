
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "PESD5V0L5UY"
    hexID = "SZKPOWERPROTECTIONPESD5VL5UY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PESD3V3L5UY', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'PESD5V0L5UY', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PESDXL5UF_V_Y.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Low capacitance unidirectional fivefold ESD protection diode array, 5.0V, Common Anode, SOT-363', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('Power_Protection : PESD5V0L5UY')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

