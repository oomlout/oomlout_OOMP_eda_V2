
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-VQ-48-1EP_7x7mm_P0.5mm"
    hexID = "FZKCSPLFCSPVQ481EP7X7P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-VQ-48-1EP_7x7mm_P0.5mm', 'description': 'LFCSP VQ, 48 pin, exposed pad, 7x7mm body (http://www.analog.com/media/en/technical-documentation/data-sheets/AD7951.pdf, http://www.analog.com/en/design-center/packaging-quality-symbols-footprints/symbols-and-footprints/AD7951.html)', 'tags': 'LFCSP 48', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-VQ-48-1EP_7x7mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_CSP : LFCSP-VQ-48-1EP_7x7mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

