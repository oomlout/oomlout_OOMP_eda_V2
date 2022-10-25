
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinHeader_2.00mm"
    oIndex = "PinHeader_2x26_P2.00mm_Horizontal"
    hexID = "FZKCNPINHEADER2PINHEADER2X26P2HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinHeader_2x26_P2.00mm_Horizontal', 'description': 'Through hole angled pin header, 2x26, 2.00mm pitch, 4.2mm pin length, double rows', 'tags': 'Through hole angled pin header THT 2x26 2.00mm double row', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinHeader_2.00mm.3dshapes/PinHeader_2x26_P2.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinHeader_2.00mm : PinHeader_2x26_P2.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

