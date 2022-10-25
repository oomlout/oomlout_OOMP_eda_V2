
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-8-1EP_2x3mm_P0.5mm_EP0.61x2.2mm"
    hexID = "FZKDFNDFN81EP2X3P5EP61X22"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-8-1EP_2x3mm_P0.5mm_EP0.61x2.2mm', 'description': 'DDB Package; 8-Lead Plastic DFN (3mm x 2mm) (see Linear Technology DFN_8_05-08-1702.pdf)', 'tags': 'DFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-8-1EP_2x3mm_P0.5mm_EP0.61x2.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-8-1EP_2x3mm_P0.5mm_EP0.61x2.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

