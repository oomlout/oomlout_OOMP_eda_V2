
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SSOP-16_3.9x4.9mm_P0.635mm"
    hexID = "FZKSOSS1639X49P635"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SSOP-16_3.9x4.9mm_P0.635mm', 'description': 'SSOP16: plastic shrink small outline package; 16 leads; body width 3.9 mm; lead pitch 0.635; (see NXP SSOP-TSSOP-VSO-REFLOW.pdf and sot519-1_po.pdf)', 'tags': 'SSOP 0.635', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSOP-16_3.9x4.9mm_P0.635mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : SSOP-16_3.9x4.9mm_P0.635mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

