
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "ADW11"
    hexID = "SZKRELAYADW11"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'ADW11', 'kicadSymbolFootprint': 'Relay_THT:Relay_1P1T_NO_10x24x18.8mm_Panasonic_ADW11xxxxW_THT', 'kicadSymbolDatasheet': 'https://www.panasonic-electric-works.com/pew/es/downloads/ds_dw_hl_en.pdf', 'kicadSymbolki_keywords': 'SPST 1P1T', 'kicadSymbolki_description': 'Panasonic, 8A/16A, Small Polarized Latching Power Relays, Single coil, 1 Form A', 'kicadSymbolki_fp_filters': 'Relay*1P1T*NO*Panasonic*ADW11xxxxW*'}])
    newPart['name'].append('ADW11')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

