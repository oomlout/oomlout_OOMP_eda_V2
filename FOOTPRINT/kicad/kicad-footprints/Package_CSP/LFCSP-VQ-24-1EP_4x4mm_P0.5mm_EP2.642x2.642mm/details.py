
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-VQ-24-1EP_4x4mm_P0.5mm_EP2.642x2.642mm"
    hexID = "FZKCSPLFCSPVQ241EP4X4P5EP2642X2642"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-VQ-24-1EP_4x4mm_P0.5mm_EP2.642x2.642mm', 'description': 'LFCSP VQ, 24 pin, exposed pad, 4x4mm body, pitch 0.5mm (http://www.analog.com/media/en/package-pcb-resources/package/56702234806764cp_24_3.pdf, http://www.analog.com/media/en/technical-documentation/data-sheets/ADL5801.pdf)', 'tags': 'LFCSP 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-VQ-24-1EP_4x4mm_P0.5mm_EP2.642x2.642mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_CSP : LFCSP-VQ-24-1EP_4x4mm_P0.5mm_EP2.642x2.642mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

