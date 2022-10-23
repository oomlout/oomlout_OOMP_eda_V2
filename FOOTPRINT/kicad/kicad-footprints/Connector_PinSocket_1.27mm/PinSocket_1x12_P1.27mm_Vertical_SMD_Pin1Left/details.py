
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinSocket_1.27mm"
    oIndex = "PinSocket_1x12_P1.27mm_Vertical_SMD_Pin1Left"
    hexID = "FZKCNPINSO127PINSO1X12P127VERTICALSMPIN1LEFT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinSocket_1x12_P1.27mm_Vertical_SMD_Pin1Left', 'description': 'surface-mounted straight socket strip, 1x12, 1.27mm pitch, single row, style 1 (pin 1 left) (https://gct.co/pdfjs/web/viewer.html?file=/Files/Drawings/BD075.pdf&t=1511594726925), script generated', 'tags': 'Surface mounted socket strip SMD 1x12 1.27mm single row style1 pin1 left', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinSocket_1.27mm.3dshapes/PinSocket_1x12_P1.27mm_Vertical_SMD_Pin1Left.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinSocket_1.27mm : PinSocket_1x12_P1.27mm_Vertical_SMD_Pin1Left')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

