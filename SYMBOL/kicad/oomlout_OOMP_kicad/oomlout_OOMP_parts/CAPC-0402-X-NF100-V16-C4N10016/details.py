
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "CAPC-0402-X-NF100-V16-C4N10016"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSCAPC42XNF1V16C4N116"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'C', 'kicadSymbolValue': 'CAPC-0402-X-NF100-V16-C4N10016', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:CAPC-0402-X-NF100-V16-C4N10016', 'kicadSymbolDatasheet': 'oom.lt/C4N10016', 'kicadSymbolki_keywords': 'cap capacitor', 'kicadSymbolki_description': 'hexID: C4N10016;PARTL C-JLCC;C1525;MANUF C-XXXX;CL05B104KO5NNNC;Unpolarized capacitor', 'kicadSymbolki_fp_filters': 'C_*'}])
    newPart['name'].append('oomlout_OOMP_parts : CAPC-0402-X-NF100-V16-C4N10016')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

