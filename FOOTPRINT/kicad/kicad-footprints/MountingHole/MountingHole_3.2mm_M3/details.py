
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "MountingHole"
    oIndex = "MountingHole_3.2mm_M3"
    hexID = "FZKHOLHOL32M3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MountingHole_3.2mm_M3', 'description': 'Mounting Hole 3.2mm, no annular, M3', 'tags': 'mounting hole 3.2mm no annular m3', 'attributeType': None, 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('MountingHole : MountingHole_3.2mm_M3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

