
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "CAPC-0603-X-PF8-V50-C6P8-C28262"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICCAPC63XPF8V5C6P8C28262"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'C', 'kicadSymbolValue': 'CAPC-0603-X-PF8-V50-C6P8-C28262', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:CAPC-0603-X-PF8-V50-C6P8-C28262', 'kicadSymbolDatasheet': 'oom.lt/C6P8', 'kicadSymbolki_keywords': 'cap capacitor', 'kicadSymbolki_description': 'hexID: C6P8;PARTL C-JLCC;C28262;MANUF C-XXXX;CL10C680JB8NNNC;Unpolarized capacitor', 'kicadSymbolki_fp_filters': 'C_*'}])
    newPart['name'].append('oomlout_OOMP_JLCC_Basic : CAPC-0603-X-PF8-V50-C6P8-C28262')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

