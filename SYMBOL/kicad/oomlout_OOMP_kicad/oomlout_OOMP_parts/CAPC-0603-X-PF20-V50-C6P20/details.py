
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "CAPC-0603-X-PF20-V50-C6P20"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSCAPC63XPF2V5C6P2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'C', 'kicadSymbolValue': 'CAPC-0603-X-PF20-V50-C6P20', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:CAPC-0603-X-PF20-V50-C6P20', 'kicadSymbolDatasheet': 'oom.lt/C6P20', 'kicadSymbolki_keywords': 'cap capacitor', 'kicadSymbolki_description': 'hexID: C6P20;PARTL C-JLCC;C1648;MANUF C-XXXX;CL10C200JB8NNNC;Unpolarized capacitor', 'kicadSymbolki_fp_filters': 'C_*'}])
    newPart['name'].append('CAPC-0603-X-PF20-V50-C6P20')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

