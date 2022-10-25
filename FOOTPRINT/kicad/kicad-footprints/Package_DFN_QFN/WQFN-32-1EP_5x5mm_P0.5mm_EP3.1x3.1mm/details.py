
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "WQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm"
    hexID = "FZKDFNWQFN321EP5X5P5EP31X31"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm', 'description': 'QFN, 32-Leads, Body 5x5x0.8mm, Pitch 0.5mm, Thermal Pad 3.1x3.1mm; (see Texas Instruments LM25119 http://www.ti.com/lit/ds/symlink/lm25119.pdf)', 'tags': 'WQFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : WQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

