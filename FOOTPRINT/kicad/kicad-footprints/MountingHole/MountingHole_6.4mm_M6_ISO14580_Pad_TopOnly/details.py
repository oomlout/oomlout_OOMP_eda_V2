
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "MountingHole"
    oIndex = "MountingHole_6.4mm_M6_ISO14580_Pad_TopOnly"
    hexID = "FZKHOLHOL64M6ISO1458PADTOPONLY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MountingHole_6.4mm_M6_ISO14580_Pad_TopOnly', 'description': 'Mounting Hole 6.4mm, M6, ISO14580', 'tags': 'mounting hole 6.4mm m6 iso14580', 'attributeType': None, 'pins': {'type': 'connect', 'shape': 'circle'}})
    newPart['name'].append('MountingHole : MountingHole_6.4mm_M6_ISO14580_Pad_TopOnly')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

