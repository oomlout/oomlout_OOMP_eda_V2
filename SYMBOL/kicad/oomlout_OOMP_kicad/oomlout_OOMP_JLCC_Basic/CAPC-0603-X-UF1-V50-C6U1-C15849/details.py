
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "CAPC-0603-X-UF1-V50-C6U1-C15849"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICCAPC63XUF1V5C6U1C15849"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'C', 'kicadSymbolValue': 'CAPC-0603-X-UF1-V50-C6U1-C15849', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:CAPC-0603-X-UF1-V50-C6U1-C15849', 'kicadSymbolDatasheet': 'oom.lt/C6U1', 'kicadSymbolki_keywords': 'cap capacitor', 'kicadSymbolki_description': 'hexID: C6U1;PARTL C-JLCC;C15849;MANUF C-XXXX;CL10A105KB8NNNC;Unpolarized capacitor', 'kicadSymbolki_fp_filters': 'C_*'}])
    newPart['name'].append('oomlout_OOMP_JLCC_Basic : CAPC-0603-X-UF1-V50-C6U1-C15849')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

