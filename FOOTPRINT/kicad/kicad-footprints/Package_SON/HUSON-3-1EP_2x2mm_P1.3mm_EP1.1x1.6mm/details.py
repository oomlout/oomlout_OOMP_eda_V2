
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "HUSON-3-1EP_2x2mm_P1.3mm_EP1.1x1.6mm"
    hexID = "FZKSONHUSON31EP2X2P13EP11X16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HUSON-3-1EP_2x2mm_P1.3mm_EP1.1x1.6mm', 'description': 'HUSON, 3 Pin, SOT1061 (Ref: https://assets.nexperia.com/documents/data-sheet/PMEG2020CPA.pdf)', 'tags': 'huson nolead SOT1061', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/HUSON-3-1EP_2x2mm_P1.3mm_EP1.1x1.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : HUSON-3-1EP_2x2mm_P1.3mm_EP1.1x1.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

