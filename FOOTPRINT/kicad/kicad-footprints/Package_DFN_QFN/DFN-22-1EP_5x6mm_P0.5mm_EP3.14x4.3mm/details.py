
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-22-1EP_5x6mm_P0.5mm_EP3.14x4.3mm"
    hexID = "FZKDFNDFN221EP5X6P5EP314X43"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-22-1EP_5x6mm_P0.5mm_EP3.14x4.3mm', 'description': 'DFN22 6*5*0.9 MM, 0.5 P; CASE 506AFxe2x88x9201 (see ON Semiconductor 506AF.PDF)', 'tags': 'DFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-22-1EP_5x6mm_P0.5mm_EP3.14x4.3mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-22-1EP_5x6mm_P0.5mm_EP3.14x4.3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

