
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinHeader_1.00mm"
    oIndex = "PinHeader_2x10_P1.00mm_Vertical_SMD"
    hexID = "FZKCNPINHEADER1PINHEADER2X1P1VERTICALSM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinHeader_2x10_P1.00mm_Vertical_SMD', 'description': 'surface-mounted straight pin header, 2x10, 1.00mm pitch, double rows', 'tags': 'Surface mounted pin header SMD 2x10 1.00mm double row', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinHeader_1.00mm.3dshapes/PinHeader_2x10_P1.00mm_Vertical_SMD.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinHeader_1.00mm : PinHeader_2x10_P1.00mm_Vertical_SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

