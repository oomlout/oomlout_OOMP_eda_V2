
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "pSemi_CSP-16_1.64x2.04mm_P0.4mm_Pad0.18mm"
    hexID = "FZKCSPPSEMICSP16164X24P4PAD18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'pSemi_CSP-16_1.64x2.04mm_P0.4mm_Pad0.18mm', 'description': 'pSemi CSP-16 1.64x2.04x0.285mm (http://www.psemi.com/pdf/datasheets/pe29101ds.pdf, http://www.psemi.com/pdf/app_notes/an77.pdf)', 'tags': 'psemi csp 16', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/pSemi_CSP-16_1.64x2.04mm_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_CSP : pSemi_CSP-16_1.64x2.04mm_P0.4mm_Pad0.18mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

