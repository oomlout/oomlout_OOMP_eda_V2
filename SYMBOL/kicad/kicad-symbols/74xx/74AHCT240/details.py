
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74AHCT240"
    hexID = "SZK74XX74AHCT24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74HC240', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74AHCT240', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/74AHCT240.pdf', 'kicadSymbolki_keywords': 'AHCTMOS BUFFER 3State inv', 'kicadSymbolki_description': '8-bit Buffer/Line Driver 3-state Inverting', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*7.5x12.8mm*P1.27mm* TSSOP*4.4x6.5mm*P0.65mm* SSOP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('74AHCT240')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

