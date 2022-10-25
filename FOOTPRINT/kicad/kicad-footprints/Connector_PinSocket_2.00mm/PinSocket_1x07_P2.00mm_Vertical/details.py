
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinSocket_2.00mm"
    oIndex = "PinSocket_1x07_P2.00mm_Vertical"
    hexID = "FZKCNPINSO2PINSO1X7P2VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinSocket_1x07_P2.00mm_Vertical', 'description': 'Through hole straight socket strip, 1x07, 2.00mm pitch, single row (from Kicad 4.0.7), script generated', 'tags': 'Through hole socket strip THT 1x07 2.00mm single row', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinSocket_2.00mm.3dshapes/PinSocket_1x07_P2.00mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinSocket_2.00mm : PinSocket_1x07_P2.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

