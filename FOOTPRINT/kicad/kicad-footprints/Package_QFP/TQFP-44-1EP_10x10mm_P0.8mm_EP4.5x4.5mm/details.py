
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "TQFP-44-1EP_10x10mm_P0.8mm_EP4.5x4.5mm"
    hexID = "FZKQFPTQFP441EP1X1P8EP45X45"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TQFP-44-1EP_10x10mm_P0.8mm_EP4.5x4.5mm', 'description': '44-Lead Plastic Thin Quad Flatpack (MW) - 10x10x1.0 mm Body [TQFP] With 4.5x4.5 mm Exposed Pad (see Microchip Packaging Specification 00000049BS.pdf)', 'tags': 'QFP 0.8', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/TQFP-44-1EP_10x10mm_P0.8mm_EP4.5x4.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_QFP : TQFP-44-1EP_10x10mm_P0.8mm_EP4.5x4.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

