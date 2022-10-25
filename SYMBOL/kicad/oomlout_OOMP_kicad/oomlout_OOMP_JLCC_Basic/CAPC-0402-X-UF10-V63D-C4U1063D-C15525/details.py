
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "CAPC-0402-X-UF10-V63D-C4U1063D-C15525"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICCAPC42XUF1V63DC4U163DC15525"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'C', 'kicadSymbolValue': 'CAPC-0402-X-UF10-V63D-C4U1063D-C15525', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:CAPC-0402-X-UF10-V63D-C4U1063D-C15525', 'kicadSymbolDatasheet': 'oom.lt/C4U1063D', 'kicadSymbolki_keywords': 'cap capacitor', 'kicadSymbolki_description': 'hexID: C4U1063D;PARTL C-JLCC;C15525;MANUF C-XXXX;CL05A106MQ5NUNC;Unpolarized capacitor', 'kicadSymbolki_fp_filters': 'C_*'}])
    newPart['name'].append('oomlout_OOMP_JLCC_Basic : CAPC-0402-X-UF10-V63D-C4U1063D-C15525')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

