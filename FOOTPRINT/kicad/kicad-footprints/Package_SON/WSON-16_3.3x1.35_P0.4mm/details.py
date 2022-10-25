
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "WSON-16_3.3x1.35_P0.4mm"
    hexID = "FZKSONWSON1633X135P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WSON-16_3.3x1.35_P0.4mm', 'description': 'WSON-16 3.3 x 1.35mm  Pitch 0.4mm http://www.chip.tomsk.ru/chip/chipdoc.nsf/Package/C67E729A4D6C883A4725793E004C8739!OpenDocument', 'tags': 'WSON-16 3.3 x 1.35mm  Pitch 0.4mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-16_3.3x1.35_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : WSON-16_3.3x1.35_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

