
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinHeader_1.00mm"
    oIndex = "PinHeader_1x14_P1.00mm_Vertical_SMD_Pin1Left"
    hexID = "FZKCNPINHEADER1PINHEADER1X14P1VERTICALSMPIN1LEFT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinHeader_1x14_P1.00mm_Vertical_SMD_Pin1Left', 'description': 'surface-mounted straight pin header, 1x14, 1.00mm pitch, single row, style 1 (pin 1 left)', 'tags': 'Surface mounted pin header SMD 1x14 1.00mm single row style1 pin1 left', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinHeader_1.00mm.3dshapes/PinHeader_1x14_P1.00mm_Vertical_SMD_Pin1Left.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinHeader_1.00mm : PinHeader_1x14_P1.00mm_Vertical_SMD_Pin1Left')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

