
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.5mm"
    hexID = "FZKDFNDFN81EP3X2P5EP13X15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.5mm', 'description': '8-Lead Plastic Dual Flat, No Lead Package (8MA2) - 2x3x0.6 mm Body [UDFN] (see Atmel-8815-SEEPROM-AT24CS01-02-Datasheet.pdf)', 'tags': 'DFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

