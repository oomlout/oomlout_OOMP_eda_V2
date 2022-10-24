
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "X2SON-8_1.4x1mm_P0.35mm"
    hexID = "FZKSONX2SON814X1P35"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'X2SON-8_1.4x1mm_P0.35mm', 'description': 'X2SON-8 1.4x1mm Pitch0.35mm http://www.ti.com/lit/ds/symlink/pca9306.pdf', 'tags': 'X2SON-8 1.4x1mm Pitch0.35mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/X2SON-8_1.4x1mm_P0.35mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : X2SON-8_1.4x1mm_P0.35mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

