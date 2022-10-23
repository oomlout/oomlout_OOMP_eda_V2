
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_FFC-FPC"
    oIndex = "Wuerth_68611214422_1x12-1MP_P1.0mm_Horizontal"
    hexID = "FZKCNFFCFPCWUERTH686112144221X121MPP1HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Wuerth_68611214422_1x12-1MP_P1.0mm_Horizontal', 'description': 'http://katalog.we-online.de/em/datasheet/68611214422.pdf', 'tags': 'Wuerth FPC 68611214422 connector 12 bottom-side contacts 1.0mm pitch 1.0mm height SMT', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/Wuerth_68611214422_1x12-1MP_P1.0mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_FFC-FPC : Wuerth_68611214422_1x12-1MP_P1.0mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

