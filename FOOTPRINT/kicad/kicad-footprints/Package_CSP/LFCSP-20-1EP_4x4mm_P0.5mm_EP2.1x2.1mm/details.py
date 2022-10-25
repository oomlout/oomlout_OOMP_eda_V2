
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-20-1EP_4x4mm_P0.5mm_EP2.1x2.1mm"
    hexID = "FZKCSPLFCSP21EP4X4P5EP21X21"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-20-1EP_4x4mm_P0.5mm_EP2.1x2.1mm', 'description': '20-Lead Frame Chip Scale Package - 4x4x0.9 mm Body [LFCSP], (see http://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/lfcspcp/cp_20_6.pdf)', 'tags': 'LFCSP 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-20-1EP_4x4mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_CSP : LFCSP-20-1EP_4x4mm_P0.5mm_EP2.1x2.1mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

