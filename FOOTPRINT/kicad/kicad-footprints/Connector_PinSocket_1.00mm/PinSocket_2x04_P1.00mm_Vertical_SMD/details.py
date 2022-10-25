
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinSocket_1.00mm"
    oIndex = "PinSocket_2x04_P1.00mm_Vertical_SMD"
    hexID = "FZKCNPINSO1PINSO2X4P1VERTICALSM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinSocket_2x04_P1.00mm_Vertical_SMD', 'description': 'surface-mounted straight socket strip, 2x04, 1.00mm pitch, double cols (https://gct.co/files/drawings/bc085.pdf), script generated', 'tags': 'Surface mounted socket strip SMD 2x04 1.00mm double row', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinSocket_1.00mm.3dshapes/PinSocket_2x04_P1.00mm_Vertical_SMD.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinSocket_1.00mm : PinSocket_2x04_P1.00mm_Vertical_SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

