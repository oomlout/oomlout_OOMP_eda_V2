
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "G5V-1"
    hexID = "SZKRELAYG5V1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'G5V-1', 'kicadSymbolFootprint': 'Relay_THT:Relay_SPDT_Omron_G5V-1', 'kicadSymbolDatasheet': 'http://omronfs.omron.com/en_US/ecb/products/pdf/en-g5v_1.pdf', 'kicadSymbolki_keywords': 'Single Pole Relay SPDT', 'kicadSymbolki_description': 'Ultra-miniature, Highly Sensitive SPDT Relay for Signal Circuits', 'kicadSymbolki_fp_filters': 'Relay*SPDT*Omron*G5V?1*'}])
    newPart['name'].append('G5V-1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

