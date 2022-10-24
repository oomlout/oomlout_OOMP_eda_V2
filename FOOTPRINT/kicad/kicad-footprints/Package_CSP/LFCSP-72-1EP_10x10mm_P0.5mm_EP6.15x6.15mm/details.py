
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-72-1EP_10x10mm_P0.5mm_EP6.15x6.15mm"
    hexID = "FZKCSPLFCSP721EP1X1P5EP615X615"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-72-1EP_10x10mm_P0.5mm_EP6.15x6.15mm', 'description': '72-Lead Frame Chip Scale Package - 10x10x0.9 mm Body [LFCSP]; (see https://www.intersil.com/content/dam/Intersil/documents/l72_/l72.10x10c.pdf)', 'tags': 'LFCSP 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-72-1EP_10x10mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_CSP : LFCSP-72-1EP_10x10mm_P0.5mm_EP6.15x6.15mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

