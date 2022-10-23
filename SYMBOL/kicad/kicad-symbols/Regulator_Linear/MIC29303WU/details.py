
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MIC29303WU"
    hexID = "SZKREGULATORLINEARMIC2933WU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MIC29153WU', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC29303WU', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-5_TabPin3', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/20005685a.pdf', 'kicadSymbolki_keywords': '3A LDO linear voltage regulator adjustable positive', 'kicadSymbolki_description': '3A low dropout linear regulator, adjustable output, TO-263', 'kicadSymbolki_fp_filters': 'TO*263*'}])
    newPart['name'].append('MIC29303WU')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

