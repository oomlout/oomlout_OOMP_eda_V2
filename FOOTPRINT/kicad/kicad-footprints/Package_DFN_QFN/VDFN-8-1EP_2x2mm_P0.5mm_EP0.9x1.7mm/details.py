
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "VDFN-8-1EP_2x2mm_P0.5mm_EP0.9x1.7mm"
    hexID = "FZKDFNVDFN81EP2X2P5EP9X17"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VDFN-8-1EP_2x2mm_P0.5mm_EP0.9x1.7mm', 'description': '8-Lead Very Thin Dual Flatpack No-Lead (LZ) - 2x3x0.9 mm Body [VDFN] (see Microchip Packaging Specification 00000049BS.pdf)', 'tags': 'DFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/VDFN-8-1EP_2x2mm_P0.5mm_EP0.9x1.7mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : VDFN-8-1EP_2x2mm_P0.5mm_EP0.9x1.7mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

