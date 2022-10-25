
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "TQFP-48-1EP_7x7mm_P0.5mm_EP3.5x3.5mm"
    hexID = "FZKQFPTQFP481EP7X7P5EP35X35"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TQFP-48-1EP_7x7mm_P0.5mm_EP3.5x3.5mm', 'description': '48-Lead Thin Quad Flatpack (PT) - 7x7x1.0 mm Body [TQFP] With Exposed Pad (see Microchip Packaging Specification 00000049BS.pdf)', 'tags': 'QFP 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/TQFP-48-1EP_7x7mm_P0.5mm_EP3.5x3.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_QFP : TQFP-48-1EP_7x7mm_P0.5mm_EP3.5x3.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

