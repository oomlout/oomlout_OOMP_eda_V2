
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "MSxx-1Axx-75"
    hexID = "SZKRELAYMSXX1AXX75"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'MSxx-1Axx-75', 'kicadSymbolFootprint': 'Relay_THT:Relay_SPST_StandexMeder_MS_Form1AB', 'kicadSymbolDatasheet': 'https://standexelectronics.com/de/produkte/ms-reed-relais/', 'kicadSymbolki_keywords': 'Single Pole Reed Relay SPST', 'kicadSymbolki_description': 'Standex Meder MS reed relay, SPST, Closing Contact', 'kicadSymbolki_fp_filters': 'Relay*SPST*StandexMeder*MS*Form1AB*'}])
    newPart['name'].append('MSxx-1Axx-75')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

