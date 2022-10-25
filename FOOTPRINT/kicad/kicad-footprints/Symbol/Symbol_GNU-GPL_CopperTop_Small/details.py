
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "Symbol_GNU-GPL_CopperTop_Small"
    hexID = "FZKSZSYGNUGPLCTOPSLL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Symbol_GNU-GPL_CopperTop_Small', 'description': 'Symbol, GNU-GPL, Copper Top, Small,', 'tags': 'Symbol, GNU-GPL, Copper Top, Small,', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : Symbol_GNU-GPL_CopperTop_Small')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

