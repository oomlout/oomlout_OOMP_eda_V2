
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-8-1EP_3x2mm_P0.5mm_EP1.6x1.65mm"
    hexID = "FZKCSPLFCSP81EP3X2P5EP16X165"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-8-1EP_3x2mm_P0.5mm_EP1.6x1.65mm', 'description': 'LFCSP 8pin Pitch 0.5mm, http://www.analog.com/media/en/package-pcb-resources/package/57080735642908cp_8_4.pdf', 'tags': 'LFCSP 8pin thermal pad 3x2mm Pitch 0.5mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-8-1EP_3x2mm_P0.5mm_EP1.6x1.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_CSP : LFCSP-8-1EP_3x2mm_P0.5mm_EP1.6x1.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

