
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "LTC6994xS6-2"
    hexID = "SZKTIMERLTC6994XS62"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC6994xS6-1', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC6994xS6-2', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-6', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/699412fb.pdf', 'kicadSymbolki_keywords': 'TimerBlox debouncer noise discriminator', 'kicadSymbolki_description': 'TimerBlox Debouncer, Programmable, Noise Discriminator, Rising and Falling Edges, TSOT-23-6', 'kicadSymbolki_fp_filters': 'TSOT*23*'}])
    newPart['name'].append('LTC6994xS6-2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

