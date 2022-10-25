
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "MountingHole"
    oIndex = "MountingHole_2.7mm_M2.5_ISO14580_Pad"
    hexID = "FZKHOLHOL27M25ISO1458PAD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MountingHole_2.7mm_M2.5_ISO14580_Pad', 'description': 'Mounting Hole 2.7mm, M2.5, ISO14580', 'tags': 'mounting hole 2.7mm m2.5 iso14580', 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('MountingHole : MountingHole_2.7mm_M2.5_ISO14580_Pad')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

