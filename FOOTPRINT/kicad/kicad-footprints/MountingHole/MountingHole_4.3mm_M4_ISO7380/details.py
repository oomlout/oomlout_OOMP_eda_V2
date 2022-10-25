
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "MountingHole"
    oIndex = "MountingHole_4.3mm_M4_ISO7380"
    hexID = "FZKHOLHOL43M4ISO738"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MountingHole_4.3mm_M4_ISO7380', 'description': 'Mounting Hole 4.3mm, no annular, M4, ISO7380', 'tags': 'mounting hole 4.3mm no annular m4 iso7380', 'attributeType': None, 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('MountingHole : MountingHole_4.3mm_M4_ISO7380')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

