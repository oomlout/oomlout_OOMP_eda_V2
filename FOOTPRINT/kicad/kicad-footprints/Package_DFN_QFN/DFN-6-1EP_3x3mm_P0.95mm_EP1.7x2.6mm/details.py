
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-6-1EP_3x3mm_P0.95mm_EP1.7x2.6mm"
    hexID = "FZKDFNDFN61EP3X3P95EP17X26"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-6-1EP_3x3mm_P0.95mm_EP1.7x2.6mm', 'description': 'DFN6 3*3 MM, 0.95 PITCH; CASE 506AH-01 (see ON Semiconductor 506AH.PDF)', 'tags': 'DFN 0.95', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-6-1EP_3x3mm_P0.95mm_EP1.7x2.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-6-1EP_3x3mm_P0.95mm_EP1.7x2.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

