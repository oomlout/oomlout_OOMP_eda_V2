
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "TPD2E2U06"
    hexID = "SZKPOWERPROTECTIONTPD2E2U6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPD2E2U06', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-543', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tpd2e2u06.pdf', 'kicadSymbolki_keywords': 'ESD-Protection', 'kicadSymbolki_description': 'Dual-Channel High-Speed ESD Protection', 'kicadSymbolki_fp_filters': 'SOT?543*'}])
    newPart['name'].append('TPD2E2U06')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

