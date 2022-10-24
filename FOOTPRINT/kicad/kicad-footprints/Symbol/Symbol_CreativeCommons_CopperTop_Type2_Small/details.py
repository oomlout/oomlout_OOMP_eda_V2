
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "Symbol_CreativeCommons_CopperTop_Type2_Small"
    hexID = "FZKSZSYCREATIVECOONSCTOPTYPE2SLL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Symbol_CreativeCommons_CopperTop_Type2_Small', 'description': 'Symbol, Creative Commons, CopperTop, Type 2, Small,', 'tags': 'Symbol, Creative Commons, CopperTop, Type 2, Small,', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : Symbol_CreativeCommons_CopperTop_Type2_Small')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

