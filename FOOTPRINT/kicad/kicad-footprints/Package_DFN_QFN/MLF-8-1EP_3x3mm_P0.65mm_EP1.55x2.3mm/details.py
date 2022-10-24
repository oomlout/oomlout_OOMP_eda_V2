
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "MLF-8-1EP_3x3mm_P0.65mm_EP1.55x2.3mm"
    hexID = "FZKDFNMLF81EP3X3P65EP155X23"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MLF-8-1EP_3x3mm_P0.65mm_EP1.55x2.3mm', 'description': '8-Pin ePad 3mm x 3mm MLF - 3x3x0.85 mm Body (see Microchip datasheet http://ww1.microchip.com/downloads/en/DeviceDoc/mic5355_6.pdf)', 'tags': 'DFN MLF 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/MLF-8-1EP_3x3mm_P0.65mm_EP1.55x2.3mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : MLF-8-1EP_3x3mm_P0.65mm_EP1.55x2.3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

