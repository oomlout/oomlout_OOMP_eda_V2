
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "CAPC-0603-X-UF22D-V10-C6U002"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSCAPC63XUF22DV1C6U2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'C', 'kicadSymbolValue': 'CAPC-0603-X-UF22D-V10-C6U002', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:CAPC-0603-X-UF22D-V10-C6U002', 'kicadSymbolDatasheet': 'oom.lt/C6U002', 'kicadSymbolki_keywords': 'cap capacitor', 'kicadSymbolki_description': 'hexID: C6U002;Unpolarized capacitor', 'kicadSymbolki_fp_filters': 'C_*'}])
    newPart['name'].append('CAPC-0603-X-UF22D-V10-C6U002')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

