
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "TSSOP-28-1EP_4.4x9.7mm_P0.65mm"
    hexID = "FZKSOTSS281EP44X97P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TSSOP-28-1EP_4.4x9.7mm_P0.65mm', 'description': 'TSSOP28: plastic thin shrink small outline package; 28 leads; body width 4.4 mm; Exposed Pad Variation; (see NXP SSOP-TSSOP-VSO-REFLOW.pdf and sot361-1_po.pdf)', 'tags': 'SSOP 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TSSOP-28_4.4x9.7mm_Pitch0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : TSSOP-28-1EP_4.4x9.7mm_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

