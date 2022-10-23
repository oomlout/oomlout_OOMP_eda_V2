
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinSocket_1.27mm"
    oIndex = "PinSocket_1x35_P1.27mm_Vertical_SMD_Pin1Right"
    hexID = "FZKCNPINSO127PINSO1X35P127VERTICALSMPIN1RIGHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinSocket_1x35_P1.27mm_Vertical_SMD_Pin1Right', 'description': 'surface-mounted straight socket strip, 1x35, 1.27mm pitch, single row, style 2 (pin 1 right) (https://gct.co/pdfjs/web/viewer.html?file=/Files/Drawings/BD075.pdf&t=1511594726925), script generated', 'tags': 'Surface mounted socket strip SMD 1x35 1.27mm single row style2 pin1 right', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinSocket_1.27mm.3dshapes/PinSocket_1x35_P1.27mm_Vertical_SMD_Pin1Right.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinSocket_1.27mm : PinSocket_1x35_P1.27mm_Vertical_SMD_Pin1Right')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

