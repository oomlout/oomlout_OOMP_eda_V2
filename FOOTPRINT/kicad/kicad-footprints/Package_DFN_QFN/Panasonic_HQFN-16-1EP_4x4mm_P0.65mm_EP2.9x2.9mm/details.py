
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Panasonic_HQFN-16-1EP_4x4mm_P0.65mm_EP2.9x2.9mm"
    hexID = "FZKDFNPHQFN161EP4X4P65EP29X29"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Panasonic_HQFN-16-1EP_4x4mm_P0.65mm_EP2.9x2.9mm', 'description': 'Panasonic HQFN-16, 4x4x0.85mm (https://industrial.panasonic.com/content/data/SC/ds/ds7/c0/PKG_HQFN016-A-0404XZL_EN.pdf)', 'tags': 'panasonic hqfn', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Panasonic_HQFN-16-1EP_4x4mm_P0.65mm_EP2.9x2.9mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : Panasonic_HQFN-16-1EP_4x4mm_P0.65mm_EP2.9x2.9mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

