
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "MountingHole"
    oIndex = "MountingHole_5.3mm_M5_DIN965_Pad"
    hexID = "FZKHOLHOL53M5DIN965PAD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MountingHole_5.3mm_M5_DIN965_Pad', 'description': 'Mounting Hole 5.3mm, M5, DIN965', 'tags': 'mounting hole 5.3mm m5 din965', 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('MountingHole : MountingHole_5.3mm_M5_DIN965_Pad')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

