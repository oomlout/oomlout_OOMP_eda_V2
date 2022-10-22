
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Buffer"
    oIndex = "LH0002H"
    hexID = "SZKAMPLIFIERBUFFERLH2H"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LH0002H', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-5-8', 'kicadSymbolDatasheet': 'http://www.calogic.net/pdf/LH0002_Datasheet_Rev_A.pdf', 'kicadSymbolki_keywords': 'Buffer', 'kicadSymbolki_description': 'Wide-Band, High Current, Unity Gain Buffer Amplifier, TO-5-8', 'kicadSymbolki_fp_filters': 'TO?5*'}])
    newPart['name'].append('LH0002H')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

