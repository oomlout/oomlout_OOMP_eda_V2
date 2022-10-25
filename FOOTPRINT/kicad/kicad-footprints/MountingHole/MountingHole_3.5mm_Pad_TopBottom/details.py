
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "MountingHole"
    oIndex = "MountingHole_3.5mm_Pad_TopBottom"
    hexID = "FZKHOLHOL35PADTOPBOTTOM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MountingHole_3.5mm_Pad_TopBottom', 'description': 'Mounting Hole 3.5mm', 'tags': 'mounting hole 3.5mm', 'attributeType': None, 'pins': {'type': 'connect', 'shape': 'circle'}})
    newPart['name'].append('MountingHole : MountingHole_3.5mm_Pad_TopBottom')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

