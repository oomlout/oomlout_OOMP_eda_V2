
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-32-1EP_4x7mm_P0.4mm_EP2.64x6.44mm"
    hexID = "FZKDFNDFN321EP4X7P4EP264X644"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-32-1EP_4x7mm_P0.4mm_EP2.64x6.44mm', 'description': 'DKD Package; 32-Lead Plastic DFN (7mm x 4mm) (see Linear Technology DFN_32_05-08-1734.pdf)', 'tags': 'DFN 0.4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-32-1EP_4x7mm_P0.4mm_EP2.64x6.44mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-32-1EP_4x7mm_P0.4mm_EP2.64x6.44mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

