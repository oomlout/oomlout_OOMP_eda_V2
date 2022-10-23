
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinSocket_2.54mm"
    oIndex = "PinSocket_1x03_P2.54mm_Vertical_SMD_Pin1Left"
    hexID = "FZKCNPINSO254PINSO1X3P254VERTICALSMPIN1LEFT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinSocket_1x03_P2.54mm_Vertical_SMD_Pin1Left', 'description': 'surface-mounted straight socket strip, 1x03, 2.54mm pitch, single row, style 1 (pin 1 left) (https://cdn.harwin.com/pdfs/M20-786.pdf), script generated', 'tags': 'Surface mounted socket strip SMD 1x03 2.54mm single row style1 pin1 left', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinSocket_2.54mm.3dshapes/PinSocket_1x03_P2.54mm_Vertical_SMD_Pin1Left.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinSocket_2.54mm : PinSocket_1x03_P2.54mm_Vertical_SMD_Pin1Left')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

