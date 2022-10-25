
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "CAPC-0402-X-PF10-V50-C4P10-C32949"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICCAPC42XPF1V5C4P1C32949"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'C', 'kicadSymbolValue': 'CAPC-0402-X-PF10-V50-C4P10-C32949', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:CAPC-0402-X-PF10-V50-C4P10-C32949', 'kicadSymbolDatasheet': 'oom.lt/C4P10', 'kicadSymbolki_keywords': 'cap capacitor', 'kicadSymbolki_description': 'hexID: C4P10;PARTL C-JLCC;C32949;MANUF C-XXXX;CL05C100JB5NNNC;Unpolarized capacitor', 'kicadSymbolki_fp_filters': 'C_*'}])
    newPart['name'].append('oomlout_OOMP_JLCC_Basic : CAPC-0402-X-PF10-V50-C4P10-C32949')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

