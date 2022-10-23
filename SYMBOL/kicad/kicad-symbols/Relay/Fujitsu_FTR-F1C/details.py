
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "Fujitsu_FTR-F1C"
    hexID = "SZKRELAYFUJITSUFTRF1C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'Fujitsu_FTR-F1C', 'kicadSymbolFootprint': 'Relay_THT:Relay_DPDT_Fujitsu_FTR-F1C', 'kicadSymbolDatasheet': 'https://www.fujitsu.com/downloads/MICRO/fcai/relays/ftr-f1.pdf', 'kicadSymbolki_keywords': 'double pole double throw relay', 'kicadSymbolki_description': 'Fujitsu Low Profile Power Relay', 'kicadSymbolki_fp_filters': '*Relay*DPDT*Fujitsu*FTR*F1C*'}])
    newPart['name'].append('Fujitsu_FTR-F1C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

