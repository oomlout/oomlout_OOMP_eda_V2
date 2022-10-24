
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SSOP-14_5.3x6.2mm_P0.65mm"
    hexID = "FZKSOSS1453X62P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SSOP-14_5.3x6.2mm_P0.65mm', 'description': 'SSOP14: plastic shrink small outline package; 14 leads; body width 5.3 mm; (see NXP SSOP-TSSOP-VSO-REFLOW.pdf and sot337-1_po.pdf)', 'tags': 'SSOP 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSOP-14_5.3x6.2mm_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : SSOP-14_5.3x6.2mm_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

