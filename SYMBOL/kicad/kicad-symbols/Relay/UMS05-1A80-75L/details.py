
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "UMS05-1A80-75L"
    hexID = "SZKRELAYUMS51A875L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'UMS05-1A80-75L', 'kicadSymbolFootprint': 'Relay_THT:Relay_StandexMeder_UMS', 'kicadSymbolDatasheet': 'https://standexelectronics.com/de/produkte/ums-reed-relais/', 'kicadSymbolki_keywords': 'Single Pole Reed Relay SPST', 'kicadSymbolki_description': 'Standex Meder UMS reed relay, SPST, Closing Contact', 'kicadSymbolki_fp_filters': 'Relay*StandexMeder*UMS*'}])
    newPart['name'].append('UMS05-1A80-75L')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

