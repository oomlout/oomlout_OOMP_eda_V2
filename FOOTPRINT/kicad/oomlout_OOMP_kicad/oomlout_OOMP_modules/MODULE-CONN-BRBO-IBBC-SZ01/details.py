
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_modules"
    oIndex = "MODULE-CONN-BRBO-IBBC-SZ01"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPMOSMOCONNBRBOIBBCSZ1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MODULE-CONN-BRBO-IBBC-SZ01', 'tags': None, 'attributeType': None, 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('oomlout_OOMP_modules : MODULE-CONN-BRBO-IBBC-SZ01')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

