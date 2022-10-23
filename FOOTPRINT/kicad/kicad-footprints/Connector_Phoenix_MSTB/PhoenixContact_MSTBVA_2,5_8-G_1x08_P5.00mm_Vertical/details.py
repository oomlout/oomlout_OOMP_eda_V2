
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MSTB"
    oIndex = "PhoenixContact_MSTBVA_2,5_8-G_1x08_P5.00mm_Vertical"
    hexID = "FZKCNPHOENIXMSTBPHOENIXCONTACTMSTBVA258G1X8P5VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MSTBVA_2,5_8-G_1x08_P5.00mm_Vertical', 'description': 'Generic Phoenix Contact connector footprint for: MSTBVA_2,5/8-G; number of pins: 08; pin pitch: 5.00mm; Vertical || order number: 1755574 12A || order number: 1924253 16A (HC)', 'tags': 'phoenix_contact connector MSTBVA_01x08_G_5.00mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MSTB.3dshapes/PhoenixContact_MSTBVA_2,5_8-G_1x08_P5.00mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_MSTB : PhoenixContact_MSTBVA_2,5_8-G_1x08_P5.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

