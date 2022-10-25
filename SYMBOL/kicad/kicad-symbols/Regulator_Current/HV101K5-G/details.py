
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Current"
    oIndex = "HV101K5-G"
    hexID = "SZKREGULATORCURRENTHV11K5G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HV100K5-G', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HV101K5-G', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'http://www.supertex.com/pdf/datasheets/HV100.pdf', 'kicadSymbolki_keywords': 'Hot-Swap Current Limiter', 'kicadSymbolki_description': 'Hot-Swap Current Limiter Controller, SOT223', 'kicadSymbolki_fp_filters': 'SOT?223*TabPin2*'}])
    newPart['name'].append('Regulator_Current : HV101K5-G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

