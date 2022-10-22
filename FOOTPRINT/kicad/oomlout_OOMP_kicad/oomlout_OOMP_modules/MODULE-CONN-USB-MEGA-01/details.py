
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_modules"
    oIndex = "MODULE-CONN-USB-MEGA-01"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPMOSMOCONNUMEGA1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MODULE-CONN-USB-MEGA-01', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'np_thru_hole', 'shape': 'oval'}})
    newPart['name'].append('oomlout_OOMP_modules : MODULE-CONN-USB-MEGA-01')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

