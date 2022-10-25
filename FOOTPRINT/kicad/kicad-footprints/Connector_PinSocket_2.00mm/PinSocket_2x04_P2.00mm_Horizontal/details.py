
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinSocket_2.00mm"
    oIndex = "PinSocket_2x04_P2.00mm_Horizontal"
    hexID = "FZKCNPINSO2PINSO2X4P2HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinSocket_2x04_P2.00mm_Horizontal', 'description': 'Through hole angled socket strip, 2x04, 2.00mm pitch, 6.35mm socket length, double cols (from Kicad 4.0.7), script generated', 'tags': 'Through hole angled socket strip THT 2x04 2.00mm double row', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinSocket_2.00mm.3dshapes/PinSocket_2x04_P2.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinSocket_2.00mm : PinSocket_2x04_P2.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

