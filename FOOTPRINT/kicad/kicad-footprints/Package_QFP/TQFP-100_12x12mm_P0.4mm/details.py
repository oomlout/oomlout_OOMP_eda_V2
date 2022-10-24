
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "TQFP-100_12x12mm_P0.4mm"
    hexID = "FZKQFPTQFP112X12P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TQFP-100_12x12mm_P0.4mm', 'description': '100-Lead Plastic Thin Quad Flatpack (PT) - 12x12x1 mm Body, 2.00 mm [TQFP] (see Microchip Packaging Specification 00000049BS.pdf)', 'tags': 'QFP 0.4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/TQFP-100_12x12mm_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_QFP : TQFP-100_12x12mm_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

