
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "UQFN-16-1EP_4x4mm_P0.65mm_EP2.7x2.7mm"
    hexID = "FZKDFNUQFN161EP4X4P65EP27X27"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UQFN-16-1EP_4x4mm_P0.65mm_EP2.7x2.7mm', 'description': '16-Lead Ultra Thin Plastic Quad Flat, No Lead Package (JQ) - 4x4x0.5 mm Body [UQFN]; (see Microchip Packaging Specification 00000049BS.pdf)', 'tags': 'QFN 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/UQFN-16-1EP_4x4mm_P0.65mm_EP2.7x2.7mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : UQFN-16-1EP_4x4mm_P0.65mm_EP2.7x2.7mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

