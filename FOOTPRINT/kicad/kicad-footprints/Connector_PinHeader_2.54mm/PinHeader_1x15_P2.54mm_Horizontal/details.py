
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinHeader_2.54mm"
    oIndex = "PinHeader_1x15_P2.54mm_Horizontal"
    hexID = "FZKCNPINHEADER254PINHEADER1X15P254HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinHeader_1x15_P2.54mm_Horizontal', 'description': 'Through hole angled pin header, 1x15, 2.54mm pitch, 6mm pin length, single row', 'tags': 'Through hole angled pin header THT 1x15 2.54mm single row', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinHeader_2.54mm.3dshapes/PinHeader_1x15_P2.54mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinHeader_2.54mm : PinHeader_1x15_P2.54mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

