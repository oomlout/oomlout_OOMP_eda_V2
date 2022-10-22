
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74HCT164"
    hexID = "SZK74XX74HCT164"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74HC164', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74HCT164', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/74HC_HCT164.pdf', 'kicadSymbolki_keywords': '8-bit shift register', 'kicadSymbolki_description': '8-bit serial-in parallel-out shift register', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7*P1.27mm* ?SSOP*P0.65mm* DIP*W7.62mm*'}])
    newPart['name'].append('74HCT164')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

