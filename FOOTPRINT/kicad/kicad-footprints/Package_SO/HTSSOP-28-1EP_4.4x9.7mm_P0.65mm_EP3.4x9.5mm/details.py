
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "HTSSOP-28-1EP_4.4x9.7mm_P0.65mm_EP3.4x9.5mm"
    hexID = "FZKSOHTSS281EP44X97P65EP34X95"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HTSSOP-28-1EP_4.4x9.7mm_P0.65mm_EP3.4x9.5mm', 'description': 'HTSSOP28: plastic thin shrink small outline package; 28 leads; body width 4.4 mm; thermal pad', 'tags': 'TSSOP HTSSOP 0.65 thermal pad', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HTSSOP-28-1EP_4.4x9.7mm_P0.65mm_EP3.4x9.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : HTSSOP-28-1EP_4.4x9.7mm_P0.65mm_EP3.4x9.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

