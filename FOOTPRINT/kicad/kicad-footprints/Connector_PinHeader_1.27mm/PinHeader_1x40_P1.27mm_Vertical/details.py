
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinHeader_1.27mm"
    oIndex = "PinHeader_1x40_P1.27mm_Vertical"
    hexID = "FZKCNPINHEADER127PINHEADER1X4P127VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinHeader_1x40_P1.27mm_Vertical', 'description': 'Through hole straight pin header, 1x40, 1.27mm pitch, single row', 'tags': 'Through hole pin header THT 1x40 1.27mm single row', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinHeader_1.27mm.3dshapes/PinHeader_1x40_P1.27mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinHeader_1.27mm : PinHeader_1x40_P1.27mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

