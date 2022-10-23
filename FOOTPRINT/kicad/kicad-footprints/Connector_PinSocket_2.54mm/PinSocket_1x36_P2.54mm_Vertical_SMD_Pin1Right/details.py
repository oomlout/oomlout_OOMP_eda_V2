
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinSocket_2.54mm"
    oIndex = "PinSocket_1x36_P2.54mm_Vertical_SMD_Pin1Right"
    hexID = "FZKCNPINSO254PINSO1X36P254VERTICALSMPIN1RIGHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinSocket_1x36_P2.54mm_Vertical_SMD_Pin1Right', 'description': 'surface-mounted straight socket strip, 1x36, 2.54mm pitch, single row, style 2 (pin 1 right) (https://cdn.harwin.com/pdfs/M20-786.pdf), script generated', 'tags': 'Surface mounted socket strip SMD 1x36 2.54mm single row style2 pin1 right', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinSocket_2.54mm.3dshapes/PinSocket_1x36_P2.54mm_Vertical_SMD_Pin1Right.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinSocket_2.54mm : PinSocket_1x36_P2.54mm_Vertical_SMD_Pin1Right')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

