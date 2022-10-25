
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "Battery_Panasonic_CR1025-VSK_Vertical_CircularHoles"
    hexID = "FZKBATBATPANASONICCR125VSKVERTICALCIRCULARH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Battery_Panasonic_CR1025-VSK_Vertical_CircularHoles', 'description': 'Panasonic CR-1025/VSK battery', 'tags': 'battery CR-1025 coin cell vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/Battery_Panasonic_CR1025-VSK_Vertical_CircularHoles.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Battery : Battery_Panasonic_CR1025-VSK_Vertical_CircularHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

