
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "TD1208"
    hexID = "SZKRFMOTD128"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TD1208', 'kicadSymbolFootprint': 'RF_Module:TD1208', 'kicadSymbolDatasheet': 'https://github.com/Telecom-Design/Documentation_TD_RF_Module/blob/master/TD1208%20Datasheet.pdf', 'kicadSymbolki_keywords': 'IOT SIGFOX', 'kicadSymbolki_description': 'High-Performance, Low-Current SIGFOX™ Gateway', 'kicadSymbolki_fp_filters': 'TD1208*'}])
    newPart['name'].append('TD1208')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

