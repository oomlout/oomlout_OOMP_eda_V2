
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-44-1EP_5x8.9mm_P0.4mm_EP3.7x8.4mm"
    hexID = "FZKDFNDFN441EP5X89P4EP37X84"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-44-1EP_5x8.9mm_P0.4mm_EP3.7x8.4mm', 'description': 'DFN44 8.9x5, 0.4P; CASE 506BU-01 (see ON Semiconductor 506BU.PDF)', 'tags': 'DFN 0.4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-44-1EP_5x8.9mm_P0.4mm_EP3.7x8.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-44-1EP_5x8.9mm_P0.4mm_EP3.7x8.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

