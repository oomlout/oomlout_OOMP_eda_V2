
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_AM_FM"
    oIndex = "SA605DK"
    hexID = "SZKRFAMFMSA65DK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SA605DK', 'kicadSymbolFootprint': 'Package_SO:SSOP-20_4.4x6.5mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/SA605.pdf', 'kicadSymbolki_keywords': 'High performance monolithic low-power FM IF system', 'kicadSymbolki_description': 'High performance monolithic low-power FM IF system, SSOP-20', 'kicadSymbolki_fp_filters': 'SSOP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('SA605DK')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

