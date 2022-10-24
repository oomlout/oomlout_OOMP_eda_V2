
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "Symbol_Attention_CopperTop_Big"
    hexID = "FZKSZSYATTENTIONCTOPBIG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Symbol_Attention_CopperTop_Big', 'description': 'Symbol, Attention, Copper Top, Big,', 'tags': 'Symbol, Attention, Copper Top, Big,', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : Symbol_Attention_CopperTop_Big')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

