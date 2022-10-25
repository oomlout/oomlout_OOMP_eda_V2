
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "USON-10_2.5x1.0mm_P0.5mm"
    hexID = "FZKSONUSON125X1P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USON-10_2.5x1.0mm_P0.5mm', 'description': 'USON-10 2.5x1.0mm_ Pitch 0.5mm http://www.ti.com/lit/ds/symlink/tpd4e02b04.pdf', 'tags': 'USON-10 2.5x1.0mm Pitch 0.5mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/USON-10_2.5x1.0mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : USON-10_2.5x1.0mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

