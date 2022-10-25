
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-18-1EP_4x5mm_P0.5mm_EP2.44x4.34mm"
    hexID = "FZKDFNDFN181EP4X5P5EP244X434"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-18-1EP_4x5mm_P0.5mm_EP2.44x4.34mm', 'description': 'DHD Package; 18-Lead Plastic DFN (5mm x 4mm) (see Linear Technology DFN_18_05-08-1778.pdf)', 'tags': 'DFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-18-1EP_4x5mm_P0.5mm_EP2.44x4.34mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-18-1EP_4x5mm_P0.5mm_EP2.44x4.34mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

