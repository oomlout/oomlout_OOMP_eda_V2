
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "UQFN-16-1EP_3x3mm_P0.5mm_EP1.75x1.75mm"
    hexID = "FZKDFNUQFN161EP3X3P5EP175X175"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UQFN-16-1EP_3x3mm_P0.5mm_EP1.75x1.75mm', 'description': '16-Lead Ultra Thin Quad Flat, No Lead Package (UC) - 3x3x0.5 mm Body [UQFN]; (see Microchip Packaging Specification 00000049BS.pdf)', 'tags': 'QFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/UQFN-16-1EP_3x3mm_P0.5mm_EP1.75x1.75mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : UQFN-16-1EP_3x3mm_P0.5mm_EP1.75x1.75mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

