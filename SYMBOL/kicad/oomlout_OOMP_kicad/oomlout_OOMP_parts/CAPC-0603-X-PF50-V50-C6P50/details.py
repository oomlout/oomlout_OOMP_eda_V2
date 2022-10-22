
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "CAPC-0603-X-PF50-V50-C6P50"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSCAPC63XPF5V5C6P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'C', 'kicadSymbolValue': 'CAPC-0603-X-PF50-V50-C6P50', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:CAPC-0603-X-PF50-V50-C6P50', 'kicadSymbolDatasheet': 'oom.lt/C6P50', 'kicadSymbolki_keywords': 'cap capacitor', 'kicadSymbolki_description': 'hexID: C6P50;PARTL C-JLCC;C1594;MANUF C-XXXX;0603B151K500NT;Unpolarized capacitor', 'kicadSymbolki_fp_filters': 'C_*'}])
    newPart['name'].append('CAPC-0603-X-PF50-V50-C6P50')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

