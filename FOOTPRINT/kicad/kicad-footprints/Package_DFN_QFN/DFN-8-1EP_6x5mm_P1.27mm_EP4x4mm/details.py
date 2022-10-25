
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-8-1EP_6x5mm_P1.27mm_EP4x4mm"
    hexID = "FZKDFNDFN81EP6X5P127EP4X4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-8-1EP_6x5mm_P1.27mm_EP4x4mm', 'description': 'DD Package; 8-Lead Plastic DFN (6mm x 5mm) (see http://www.everspin.com/file/236/download)', 'tags': 'dfn ', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-8-1EP_6x5mm_Pitch1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-8-1EP_6x5mm_P1.27mm_EP4x4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

