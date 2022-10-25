
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "CAPC-0402-X-NF47D-V50-C4N47D-C1538"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICCAPC42XNF47DV5C4N47DC1538"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'C', 'kicadSymbolValue': 'CAPC-0402-X-NF47D-V50-C4N47D-C1538', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:CAPC-0402-X-NF47D-V50-C4N47D-C1538', 'kicadSymbolDatasheet': 'oom.lt/C4N47D', 'kicadSymbolki_keywords': 'cap capacitor', 'kicadSymbolki_description': 'hexID: C4N47D;PARTL C-JLCC;C1538;MANUF C-XXXX;0402B472K500NT;Unpolarized capacitor', 'kicadSymbolki_fp_filters': 'C_*'}])
    newPart['name'].append('oomlout_OOMP_JLCC_Basic : CAPC-0402-X-NF47D-V50-C4N47D-C1538')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

