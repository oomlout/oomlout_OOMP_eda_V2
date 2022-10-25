
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "WQFN-20-1EP_2.5x4.5mm_P0.5mm_EP1x2.9mm"
    hexID = "FZKDFNWQFN21EP25X45P5EP1X29"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WQFN-20-1EP_2.5x4.5mm_P0.5mm_EP1x2.9mm', 'description': 'http://www.onsemi.com/pub/Collateral/510CD.PDF', 'tags': 'WQFN-20 4.5mm 2.5mm 0.5mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WQFN-20-1EP_2.5x4.5mm_P0.5mm_EP1x2.9mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : WQFN-20-1EP_2.5x4.5mm_P0.5mm_EP1x2.9mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

