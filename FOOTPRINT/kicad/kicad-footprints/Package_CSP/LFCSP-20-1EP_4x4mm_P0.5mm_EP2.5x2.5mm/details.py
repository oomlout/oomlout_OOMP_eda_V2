
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-20-1EP_4x4mm_P0.5mm_EP2.5x2.5mm"
    hexID = "FZKCSPLFCSP21EP4X4P5EP25X25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-20-1EP_4x4mm_P0.5mm_EP2.5x2.5mm', 'description': 'LFCSP, 20 Pin (https://www.analog.com/media/en/technical-documentation/data-sheets/AD7682_7689.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py', 'tags': 'LFCSP DFN_QFN', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-20-1EP_4x4mm_P0.5mm_EP2.5x2.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_CSP : LFCSP-20-1EP_4x4mm_P0.5mm_EP2.5x2.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

