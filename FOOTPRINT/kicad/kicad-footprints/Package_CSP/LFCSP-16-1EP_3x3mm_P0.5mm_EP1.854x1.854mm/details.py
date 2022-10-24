
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-16-1EP_3x3mm_P0.5mm_EP1.854x1.854mm"
    hexID = "FZKCSPLFCSP161EP3X3P5EP1854X1854"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-16-1EP_3x3mm_P0.5mm_EP1.854x1.854mm', 'description': '16-Lead Lead Frame Chip Scale Package, 3x3mm, 0.5mm pitch, 1.854mm thermal pad (CP-16-22, http://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/lfcspcp/cp_16_22.pdf)', 'tags': 'LFCSP 16 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-16-1EP_3x3mm_P0.5mm_EP1.854x1.854mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_CSP : LFCSP-16-1EP_3x3mm_P0.5mm_EP1.854x1.854mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

