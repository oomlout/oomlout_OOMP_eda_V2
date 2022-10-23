
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MSTB"
    oIndex = "PhoenixContact_MSTBA_2,5_12-G_1x12_P5.00mm_Horizontal"
    hexID = "FZKCNPHOENIXMSTBPHOENIXCONTACTMSTBA2512G1X12P5HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MSTBA_2,5_12-G_1x12_P5.00mm_Horizontal', 'description': 'Generic Phoenix Contact connector footprint for: MSTBA_2,5/12-G; number of pins: 12; pin pitch: 5.00mm; Angled || order number: 1757569 12A || order number: 1923856 16A (HC)', 'tags': 'phoenix_contact connector MSTBA_01x12_G_5.00mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MSTB.3dshapes/PhoenixContact_MSTBA_2,5_12-G_1x12_P5.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_MSTB : PhoenixContact_MSTBA_2,5_12-G_1x12_P5.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

