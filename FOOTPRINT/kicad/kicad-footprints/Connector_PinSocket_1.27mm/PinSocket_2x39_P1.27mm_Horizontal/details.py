
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinSocket_1.27mm"
    oIndex = "PinSocket_2x39_P1.27mm_Horizontal"
    hexID = "FZKCNPINSO127PINSO2X39P127HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinSocket_2x39_P1.27mm_Horizontal', 'description': 'Through hole angled socket strip, 2x39, 1.27mm pitch, 4.4mm socket length, double cols (https://gct.co/pdfjs/web/viewer.html?file=/Files/Drawings/BD091.pdf&t=1511594177220), script generated', 'tags': 'Through hole angled socket strip THT 2x39 1.27mm double row', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinSocket_1.27mm.3dshapes/PinSocket_2x39_P1.27mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinSocket_1.27mm : PinSocket_2x39_P1.27mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

