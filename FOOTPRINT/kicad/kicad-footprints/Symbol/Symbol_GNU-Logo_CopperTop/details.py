
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "Symbol_GNU-Logo_CopperTop"
    hexID = "FZKSZSYGNULCTOP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Symbol_GNU-Logo_CopperTop', 'description': 'GNU-Logo, GNU-Head, GNU-Kopf, Copper Top,', 'tags': 'GNU-Logo, GNU-Head, GNU-Kopf, Copper Top,', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : Symbol_GNU-Logo_CopperTop')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

