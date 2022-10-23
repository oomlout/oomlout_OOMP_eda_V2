
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinSocket_1.27mm"
    oIndex = "PinSocket_2x05_P1.27mm_Vertical_SMD"
    hexID = "FZKCNPINSO127PINSO2X5P127VERTICALSM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinSocket_2x05_P1.27mm_Vertical_SMD', 'description': 'surface-mounted straight socket strip, 2x05, 1.27mm pitch, double cols (from Kicad 4.0.7!), script generated', 'tags': 'Surface mounted socket strip SMD 2x05 1.27mm double row', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinSocket_1.27mm.3dshapes/PinSocket_2x05_P1.27mm_Vertical_SMD.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinSocket_1.27mm : PinSocket_2x05_P1.27mm_Vertical_SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

