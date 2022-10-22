
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "CAPC-0402-X-NF220-V16-C42N220"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSCAPC42XNF22V16C42N22"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'C', 'kicadSymbolValue': 'CAPC-0402-X-NF220-V16-C42N220', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:CAPC-0402-X-NF220-V16-C42N220', 'kicadSymbolDatasheet': 'oom.lt/C42N220', 'kicadSymbolki_keywords': 'cap capacitor', 'kicadSymbolki_description': 'hexID: C42N220;Unpolarized capacitor', 'kicadSymbolki_fp_filters': 'C_*'}])
    newPart['name'].append('CAPC-0402-X-NF220-V16-C42N220')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

