
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinHeader_2.00mm"
    oIndex = "PinHeader_1x21_P2.00mm_Vertical_SMD_Pin1Right"
    hexID = "FZKCNPINHEADER2PINHEADER1X21P2VERTICALSMPIN1RIGHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinHeader_1x21_P2.00mm_Vertical_SMD_Pin1Right', 'description': 'surface-mounted straight pin header, 1x21, 2.00mm pitch, single row, style 2 (pin 1 right)', 'tags': 'Surface mounted pin header SMD 1x21 2.00mm single row style2 pin1 right', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinHeader_2.00mm.3dshapes/PinHeader_1x21_P2.00mm_Vertical_SMD_Pin1Right.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinHeader_2.00mm : PinHeader_1x21_P2.00mm_Vertical_SMD_Pin1Right')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

