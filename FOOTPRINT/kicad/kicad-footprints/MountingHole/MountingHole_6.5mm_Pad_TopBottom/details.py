
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "MountingHole"
    oIndex = "MountingHole_6.5mm_Pad_TopBottom"
    hexID = "FZKHOLHOL65PADTOPBOTTOM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MountingHole_6.5mm_Pad_TopBottom', 'description': 'Mounting Hole 6.5mm', 'tags': 'mounting hole 6.5mm', 'attributeType': None, 'pins': {'type': 'connect', 'shape': 'circle'}})
    newPart['name'].append('MountingHole : MountingHole_6.5mm_Pad_TopBottom')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

