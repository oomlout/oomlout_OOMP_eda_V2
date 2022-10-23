
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "MountingHole"
    oIndex = "MountingHole_3.2mm_M3_DIN965_Pad_TopOnly"
    hexID = "FZKHOLHOL32M3DIN965PADTOPONLY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MountingHole_3.2mm_M3_DIN965_Pad_TopOnly', 'description': 'Mounting Hole 3.2mm, M3, DIN965', 'tags': 'mounting hole 3.2mm m3 din965', 'attributeType': None, 'pins': {'type': 'connect', 'shape': 'circle'}})
    newPart['name'].append('MountingHole : MountingHole_3.2mm_M3_DIN965_Pad_TopOnly')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

