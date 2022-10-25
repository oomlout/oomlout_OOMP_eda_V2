
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "WSON-6_1.5x1.5mm_P0.5mm"
    hexID = "FZKSONWSON615X15P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WSON-6_1.5x1.5mm_P0.5mm', 'description': 'WSON6, http://www.ti.com/lit/ds/symlink/tlv702.pdf', 'tags': 'WSON6_1.5x1.5mm_P0.5mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-6_1.5x1.5mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : WSON-6_1.5x1.5mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

