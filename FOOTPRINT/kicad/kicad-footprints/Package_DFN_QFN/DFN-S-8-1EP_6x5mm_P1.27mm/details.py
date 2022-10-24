
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-S-8-1EP_6x5mm_P1.27mm"
    hexID = "FZKDFNDFNS81EP6X5P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-S-8-1EP_6x5mm_P1.27mm', 'description': '8-Lead Plastic Dual Flat, No Lead Package (MF) - 6x5 mm Body [DFN-S] (see Microchip Packaging Specification 00000049BS.pdf)', 'tags': 'DFN 1.27', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-S-8-1EP_6x5mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'oval'}})
    newPart['name'].append('Package_DFN_QFN : DFN-S-8-1EP_6x5mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

