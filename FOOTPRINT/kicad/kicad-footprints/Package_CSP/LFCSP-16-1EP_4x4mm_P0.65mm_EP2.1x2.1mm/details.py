
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-16-1EP_4x4mm_P0.65mm_EP2.1x2.1mm"
    hexID = "FZKCSPLFCSP161EP4X4P65EP21X21"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-16-1EP_4x4mm_P0.65mm_EP2.1x2.1mm', 'description': 'LFCSP, 16 pin, 4x4mm, 2.1mm sq pad (http://www.analog.com/media/en/technical-documentation/data-sheets/ADG633.pdf)', 'tags': 'LFCSP 16 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-16-1EP_4x4mm_P0.65mm_EP2.1x2.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_CSP : LFCSP-16-1EP_4x4mm_P0.65mm_EP2.1x2.1mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

