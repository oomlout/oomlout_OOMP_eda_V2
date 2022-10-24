
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "Symbol_Highvoltage_Type2_CopperTop_Small"
    hexID = "FZKSZSYHIGHVOLTAGETYPE2CTOPSLL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Symbol_Highvoltage_Type2_CopperTop_Small', 'description': 'Symbol, Highvoltage, Type 2, Copper Top, Small,', 'tags': 'Symbol, Highvoltage, Type 2, Copper Top, Small,', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : Symbol_Highvoltage_Type2_CopperTop_Small')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

