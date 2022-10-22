
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_modules"
    oIndex = "MODULE-CONN-RASP-PICO-2040"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPMOSMOCONNRASPPICO24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MODULE-CONN-RASP-PICO-2040', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('oomlout_OOMP_modules : MODULE-CONN-RASP-PICO-2040')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

