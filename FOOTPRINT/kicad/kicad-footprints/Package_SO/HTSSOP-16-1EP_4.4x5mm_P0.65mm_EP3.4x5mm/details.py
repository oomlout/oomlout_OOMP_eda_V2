
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "HTSSOP-16-1EP_4.4x5mm_P0.65mm_EP3.4x5mm"
    hexID = "FZKSOHTSS161EP44X5P65EP34X5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HTSSOP-16-1EP_4.4x5mm_P0.65mm_EP3.4x5mm', 'description': '16-Lead Plastic HTSSOP (4.4x5x1.2mm); Thermal pad; (http://www.ti.com/lit/ds/symlink/drv8833.pdf)', 'tags': 'SSOP 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TSSOP-16-1EP_4.4x5mm_Pitch0.65mm_EP3.4x5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : HTSSOP-16-1EP_4.4x5mm_P0.65mm_EP3.4x5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

