
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "CAPC-0603-X-PF10-V50-C6P10-C1634"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICCAPC63XPF1V5C6P1C1634"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'C', 'kicadSymbolValue': 'CAPC-0603-X-PF10-V50-C6P10-C1634', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:CAPC-0603-X-PF10-V50-C6P10-C1634', 'kicadSymbolDatasheet': 'oom.lt/C6P10', 'kicadSymbolki_keywords': 'cap capacitor', 'kicadSymbolki_description': 'hexID: C6P10;PARTL C-JLCC;C1634;MANUF C-XXXX;CL10C100JB8NNNC;Unpolarized capacitor', 'kicadSymbolki_fp_filters': 'C_*'}])
    newPart['name'].append('oomlout_OOMP_JLCC_Basic : CAPC-0603-X-PF10-V50-C6P10-C1634')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

