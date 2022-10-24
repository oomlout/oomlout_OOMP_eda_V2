
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-32-1EP_5x5mm_P0.5mm_EP3.25x3.25mm"
    hexID = "FZKCSPLFCSP321EP5X5P5EP325X325"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-32-1EP_5x5mm_P0.5mm_EP3.25x3.25mm', 'description': '32-Lead Frame Chip Scale Package LFCSP (5mm x 5mm); (see http://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/lfcspcp/cp-32/CP_32_27.pdf', 'tags': 'LFCSP 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-32-1EP_5x5mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_CSP : LFCSP-32-1EP_5x5mm_P0.5mm_EP3.25x3.25mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

