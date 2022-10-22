
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "CAPC-0402-X-PF27-V50-C42P027"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSCAPC42XPF27V5C42P27"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'C', 'kicadSymbolValue': 'CAPC-0402-X-PF27-V50-C42P027', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:CAPC-0402-X-PF27-V50-C42P027', 'kicadSymbolDatasheet': 'oom.lt/C42P027', 'kicadSymbolki_keywords': 'cap capacitor', 'kicadSymbolki_description': 'hexID: C42P027;Unpolarized capacitor', 'kicadSymbolki_fp_filters': 'C_*'}])
    newPart['name'].append('CAPC-0402-X-PF27-V50-C42P027')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

