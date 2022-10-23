
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinHeader_1.27mm"
    oIndex = "PinHeader_2x04_P1.27mm_Vertical_SMD"
    hexID = "FZKCNPINHEADER127PINHEADER2X4P127VERTICALSM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinHeader_2x04_P1.27mm_Vertical_SMD', 'description': 'surface-mounted straight pin header, 2x04, 1.27mm pitch, double rows', 'tags': 'Surface mounted pin header SMD 2x04 1.27mm double row', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinHeader_1.27mm.3dshapes/PinHeader_2x04_P1.27mm_Vertical_SMD.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinHeader_1.27mm : PinHeader_2x04_P1.27mm_Vertical_SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

