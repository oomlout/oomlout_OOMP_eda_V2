
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_modules"
    oIndex = "MODULE-CONN-BRBO-IBBC-SZ01"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPMOSMOCONNBRBOIBBCSZ1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MODULE-CONN-BRBO-IBBC-SZ01', 'kicadSymbolFootprint': 'oomlout_OOMP_modules:MODULE-CONN-BRBO-IBBC-SZ01', 'kicadSymbolDatasheet': 'oom.lt/MCBI1'}])
    newPart['name'].append('MODULE-CONN-BRBO-IBBC-SZ01')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

