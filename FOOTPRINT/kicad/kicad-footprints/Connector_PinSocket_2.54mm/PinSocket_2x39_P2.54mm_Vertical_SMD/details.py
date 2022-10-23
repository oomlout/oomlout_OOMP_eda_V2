
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinSocket_2.54mm"
    oIndex = "PinSocket_2x39_P2.54mm_Vertical_SMD"
    hexID = "FZKCNPINSO254PINSO2X39P254VERTICALSM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinSocket_2x39_P2.54mm_Vertical_SMD', 'description': 'surface-mounted straight socket strip, 2x39, 2.54mm pitch, double cols (from Kicad 4.0.7), script generated', 'tags': 'Surface mounted socket strip SMD 2x39 2.54mm double row', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinSocket_2.54mm.3dshapes/PinSocket_2x39_P2.54mm_Vertical_SMD.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinSocket_2.54mm : PinSocket_2x39_P2.54mm_Vertical_SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

