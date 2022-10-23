
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinSocket_2.00mm"
    oIndex = "PinSocket_1x15_P2.00mm_Vertical_SMD_Pin1Left"
    hexID = "FZKCNPINSO2PINSO1X15P2VERTICALSMPIN1LEFT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinSocket_1x15_P2.00mm_Vertical_SMD_Pin1Left', 'description': 'surface-mounted straight socket strip, 1x15, 2.00mm pitch, single row, style 1 (pin 1 left) (https://www.jayconsystems.com/fileuploader/download/download/?d=1&file=custom%2Fupload%2FFile-1375728122.pdf), script generated', 'tags': 'Surface mounted socket strip SMD 1x15 2.00mm single row style1 pin1 left', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinSocket_2.00mm.3dshapes/PinSocket_1x15_P2.00mm_Vertical_SMD_Pin1Left.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinSocket_2.00mm : PinSocket_1x15_P2.00mm_Vertical_SMD_Pin1Left')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

