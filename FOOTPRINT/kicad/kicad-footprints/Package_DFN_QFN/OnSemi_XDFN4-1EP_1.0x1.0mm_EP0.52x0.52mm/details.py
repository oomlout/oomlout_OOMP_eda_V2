
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "OnSemi_XDFN4-1EP_1.0x1.0mm_EP0.52x0.52mm"
    hexID = "FZKDFNONSEMIXDFN41EP1X1EP52X52"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'OnSemi_XDFN4-1EP_1.0x1.0mm_EP0.52x0.52mm', 'description': 'XDFN4 footprint (as found on the https://www.onsemi.com/pub/Collateral/NCP115-D.PDF)', 'tags': 'OnSemi XDFN4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/OnSemi_XDFN4-1EP_1.0x1.0mm_EP0.52x0.52mm.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Package_DFN_QFN : OnSemi_XDFN4-1EP_1.0x1.0mm_EP0.52x0.52mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

