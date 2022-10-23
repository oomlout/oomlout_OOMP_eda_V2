
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PinHeader_1.00mm"
    oIndex = "PinHeader_1x19_P1.00mm_Vertical"
    hexID = "FZKCNPINHEADER1PINHEADER1X19P1VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PinHeader_1x19_P1.00mm_Vertical', 'description': 'Through hole straight pin header, 1x19, 1.00mm pitch, single row', 'tags': 'Through hole pin header THT 1x19 1.00mm single row', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinHeader_1.00mm.3dshapes/PinHeader_1x19_P1.00mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_PinHeader_1.00mm : PinHeader_1x19_P1.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

