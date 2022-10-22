
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "CAPC-0603-X-UF10-V25-C6U10-C96446"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICCAPC63XUF1V25C6U1C96446"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'C', 'kicadSymbolValue': 'CAPC-0603-X-UF10-V25-C6U10-C96446', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:CAPC-0603-X-UF10-V25-C6U10-C96446', 'kicadSymbolDatasheet': 'oom.lt/C6U10', 'kicadSymbolki_keywords': 'cap capacitor', 'kicadSymbolki_description': 'hexID: C6U10;PARTL C-JLCC;C96446;MANUF C-XXXX;CL10A106MA8NRNC;Unpolarized capacitor', 'kicadSymbolki_fp_filters': 'C_*'}])
    newPart['name'].append('CAPC-0603-X-UF10-V25-C6U10-C96446')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

