
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_AM_FM"
    oIndex = "SA605D"
    hexID = "SZKRFAMFMSA65D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SA605D', 'kicadSymbolFootprint': 'Package_SO:SO-20_12.8x7.5mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/SA605.pdf', 'kicadSymbolki_keywords': 'High performance monolithic low-power FM IF system', 'kicadSymbolki_description': 'High performance monolithic low-power FM IF system, SO-20', 'kicadSymbolki_fp_filters': 'SO*12.8x7.5mm*P1.27mm*'}])
    newPart['name'].append('RF_AM_FM : SA605D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

