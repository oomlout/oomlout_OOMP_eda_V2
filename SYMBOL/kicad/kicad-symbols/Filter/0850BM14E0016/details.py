
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Filter"
    oIndex = "0850BM14E0016"
    hexID = "SZKFIL85BM14E16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'FL', 'kicadSymbolValue': '0850BM14E0016', 'kicadSymbolFootprint': 'RF_Converter:Balun_Johanson_1.6x0.8mm', 'kicadSymbolDatasheet': 'https://www.johansontechnology.com/datasheets/0850BM14E0016/0850BM14E0016.pdf', 'kicadSymbolki_keywords': 'Sub-GHz Balun', 'kicadSymbolki_description': 'Sub-GHz Impedance Matched Balun + LPF integrated Passive', 'kicadSymbolki_fp_filters': 'Balun*Johanson*1.6x0.8mm*'}])
    newPart['name'].append('0850BM14E0016')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

