
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74AHCT123"
    hexID = "SZK74XX74AHCT123"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LS123', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74AHCT123', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74ahct123a', 'kicadSymbolki_keywords': 'TTL monostable, multivibrator', 'kicadSymbolki_description': 'Dual retriggerable monostable multivibrator', 'kicadSymbolki_fp_filters': 'DIP?16*'}])
    newPart['name'].append('74AHCT123')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

