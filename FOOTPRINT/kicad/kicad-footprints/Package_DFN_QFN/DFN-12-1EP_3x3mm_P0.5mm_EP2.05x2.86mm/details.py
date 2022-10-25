
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-12-1EP_3x3mm_P0.5mm_EP2.05x2.86mm"
    hexID = "FZKDFNDFN121EP3X3P5EP25X286"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-12-1EP_3x3mm_P0.5mm_EP2.05x2.86mm', 'description': '10-Lead Plastic Dual Flat, No Lead Package (MF) - 3x3x0.9 mm Body [DFN] (see Microchip Packaging Specification 00000049BS.pdf)', 'tags': 'DFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-12-1EP_3x3mm_P0.5mm_EP2.05x2.86mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-12-1EP_3x3mm_P0.5mm_EP2.05x2.86mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

