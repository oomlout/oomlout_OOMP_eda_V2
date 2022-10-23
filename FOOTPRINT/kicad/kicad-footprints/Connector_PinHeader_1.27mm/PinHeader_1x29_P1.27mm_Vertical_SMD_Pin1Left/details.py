
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinHeader_1.27mm"
    oIndex = "PinHeader_1x29_P1.27mm_Vertical_SMD_Pin1Left"
    hexID = "FZKCNPINHEADER127PINHEADER1X29P127VERTICALSMPIN1LEFT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinHeader_1x29_P1.27mm_Vertical_SMD_Pin1Left', 'description': 'surface-mounted straight pin header, 1x29, 1.27mm pitch, single row, style 1 (pin 1 left)', 'tags': 'Surface mounted pin header SMD 1x29 1.27mm single row style1 pin1 left', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinHeader_1.27mm.3dshapes/PinHeader_1x29_P1.27mm_Vertical_SMD_Pin1Left.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinHeader_1.27mm : PinHeader_1x29_P1.27mm_Vertical_SMD_Pin1Left')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

