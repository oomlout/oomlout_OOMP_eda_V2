
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "MountingHole"
    oIndex = "MountingHole_2.7mm_M2.5_ISO7380"
    hexID = "FZKHOLHOL27M25ISO738"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MountingHole_2.7mm_M2.5_ISO7380', 'description': 'Mounting Hole 2.7mm, no annular, M2.5, ISO7380', 'tags': 'mounting hole 2.7mm no annular m2.5 iso7380', 'attributeType': None, 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('MountingHole : MountingHole_2.7mm_M2.5_ISO7380')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

