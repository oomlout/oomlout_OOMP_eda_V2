
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "SD24_SOD323"
    hexID = "SZKDIODESD24SOD323"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SD05_SOD323', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SD24_SOD323', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-323', 'kicadSymbolDatasheet': 'https://www.littelfuse.com/~/media/electronics/datasheets/tvs_diode_arrays/littelfuse_tvs_diode_array_sd_c_datasheet.pdf.pdf', 'kicadSymbolki_keywords': 'transient voltage suppressor thyrector transil', 'kicadSymbolki_description': '24V, 450W Discrete Bidirectional TVS Diode, SOD-323', 'kicadSymbolki_fp_filters': 'D?SOD?323*'}])
    newPart['name'].append('SD24_SOD323')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

