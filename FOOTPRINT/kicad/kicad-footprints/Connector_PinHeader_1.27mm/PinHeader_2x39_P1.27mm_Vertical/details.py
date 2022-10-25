
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinHeader_1.27mm"
    oIndex = "PinHeader_2x39_P1.27mm_Vertical"
    hexID = "FZKCNPINHEADER127PINHEADER2X39P127VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinHeader_2x39_P1.27mm_Vertical', 'description': 'Through hole straight pin header, 2x39, 1.27mm pitch, double rows', 'tags': 'Through hole pin header THT 2x39 1.27mm double row', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinHeader_1.27mm.3dshapes/PinHeader_2x39_P1.27mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinHeader_1.27mm : PinHeader_2x39_P1.27mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

