
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "MountingHole"
    oIndex = "MountingHole_4.3x6.2mm_M4_Pad_Via"
    hexID = "FZKHOLHOL43X62M4PADVIA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MountingHole_4.3x6.2mm_M4_Pad_Via', 'description': 'Mounting Hole 4.3x6.2mm, M4', 'tags': 'mounting hole 4.3x6.2mm m4', 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('MountingHole : MountingHole_4.3x6.2mm_M4_Pad_Via')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

