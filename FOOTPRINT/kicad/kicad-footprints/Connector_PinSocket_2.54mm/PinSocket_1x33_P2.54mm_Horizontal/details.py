
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinSocket_2.54mm"
    oIndex = "PinSocket_1x33_P2.54mm_Horizontal"
    hexID = "FZKCNPINSO254PINSO1X33P254HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinSocket_1x33_P2.54mm_Horizontal', 'description': 'Through hole angled socket strip, 1x33, 2.54mm pitch, 8.51mm socket length, single row (from Kicad 4.0.7), script generated', 'tags': 'Through hole angled socket strip THT 1x33 2.54mm single row', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinSocket_2.54mm.3dshapes/PinSocket_1x33_P2.54mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinSocket_2.54mm : PinSocket_1x33_P2.54mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

