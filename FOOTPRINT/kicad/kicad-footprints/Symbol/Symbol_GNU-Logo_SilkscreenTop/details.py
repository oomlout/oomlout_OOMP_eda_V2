
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "Symbol_GNU-Logo_SilkscreenTop"
    hexID = "FZKSZSYGNULSILKSCREENTOP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Symbol_GNU-Logo_SilkscreenTop', 'description': 'GNU-Logo, GNU-Head, GNU-Kopf, Silkscreen,', 'tags': 'GNU-Logo, GNU-Head, GNU-Kopf, Silkscreen,', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : Symbol_GNU-Logo_SilkscreenTop')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

