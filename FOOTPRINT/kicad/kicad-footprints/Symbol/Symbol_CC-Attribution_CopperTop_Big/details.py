
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "Symbol_CC-Attribution_CopperTop_Big"
    hexID = "FZKSZSYCCATTRIBUTIONCTOPBIG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Symbol_CC-Attribution_CopperTop_Big', 'description': 'Symbol, CC-Attribution, Copper Top, Big,', 'tags': 'Symbol, CC-Attribution, Copper Top, Big,', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : Symbol_CC-Attribution_CopperTop_Big')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

