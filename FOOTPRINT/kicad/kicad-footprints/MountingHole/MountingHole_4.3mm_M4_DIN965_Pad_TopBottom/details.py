
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "MountingHole"
    oIndex = "MountingHole_4.3mm_M4_DIN965_Pad_TopBottom"
    hexID = "FZKHOLHOL43M4DIN965PADTOPBOTTOM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MountingHole_4.3mm_M4_DIN965_Pad_TopBottom', 'description': 'Mounting Hole 4.3mm, M4, DIN965', 'tags': 'mounting hole 4.3mm m4 din965', 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('MountingHole : MountingHole_4.3mm_M4_DIN965_Pad_TopBottom')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

