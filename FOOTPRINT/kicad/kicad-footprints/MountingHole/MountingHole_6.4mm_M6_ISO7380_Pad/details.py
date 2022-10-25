
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "MountingHole"
    oIndex = "MountingHole_6.4mm_M6_ISO7380_Pad"
    hexID = "FZKHOLHOL64M6ISO738PAD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MountingHole_6.4mm_M6_ISO7380_Pad', 'description': 'Mounting Hole 6.4mm, M6, ISO7380', 'tags': 'mounting hole 6.4mm m6 iso7380', 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('MountingHole : MountingHole_6.4mm_M6_ISO7380_Pad')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

