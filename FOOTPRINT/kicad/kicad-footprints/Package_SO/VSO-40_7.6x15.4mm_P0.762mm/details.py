
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "VSO-40_7.6x15.4mm_P0.762mm"
    hexID = "FZKSOVSO476X154P762"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VSO-40_7.6x15.4mm_P0.762mm', 'description': 'VSO40: plastic very small outline package; 40 leads (see NXP SSOP-TSSOP-VSO-REFLOW.pdf and sot158-1_po.pdf)', 'tags': 'SSOP 0.762', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/VSO-40_7.6x15.4mm_P0.762mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : VSO-40_7.6x15.4mm_P0.762mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

