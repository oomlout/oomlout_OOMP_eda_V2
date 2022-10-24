
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "MLPQ-16-1EP_4x4mm_P0.65mm_EP2.8x2.8mm"
    hexID = "FZKDFNMLPQ161EP4X4P65EP28X28"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MLPQ-16-1EP_4x4mm_P0.65mm_EP2.8x2.8mm', 'description': 'Micro Leadframe Package, 16 pin with exposed pad', 'tags': 'MLPQ- 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/MLPQ-16-1EP_4x4mm_P0.65mm_EP2.8x2.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : MLPQ-16-1EP_4x4mm_P0.65mm_EP2.8x2.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

