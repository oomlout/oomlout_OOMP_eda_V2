
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "OnSemi_UDFN-8_1.2x1.8mm_P0.4mm"
    hexID = "FZKDFNONSEMIUDFN812X18P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'OnSemi_UDFN-8_1.2x1.8mm_P0.4mm', 'description': '8-Lead Plastic Dual Flat, No Lead Package, 1.2x1.8x1.55 mm Body [UDFN] (See http://www.onsemi.com/pub/Collateral/NLSV2T244-D.PDF)', 'tags': 'dfn udfn dual flat', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/OnSemi_UDFN-8_1.2x1.8mm_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : OnSemi_UDFN-8_1.2x1.8mm_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

