
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "TQFP-80-1EP_14x14mm_P0.65mm_EP9.5x9.5mm"
    hexID = "FZKQFPTQFP81EP14X14P65EP95X95"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TQFP-80-1EP_14x14mm_P0.65mm_EP9.5x9.5mm', 'description': '80-Lead Plastic Thin Quad Flatpack (PF) - 14x14mm body, 9.5mm sq thermal pad (http://www.analog.com/media/en/technical-documentation/data-sheets/AD9852.pdf)', 'tags': 'QFP 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/TQFP-80-1EP_14x14mm_P0.65mm_EP9.5x9.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_QFP : TQFP-80-1EP_14x14mm_P0.65mm_EP9.5x9.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

