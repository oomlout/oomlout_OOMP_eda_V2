
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MSTB"
    oIndex = "PhoenixContact_MSTBA_2,5_7-G-5,08_1x07_P5.08mm_Horizontal"
    hexID = "FZKCNPHOENIXMSTBPHOENIXCONTACTMSTBA257G581X7P58HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MSTBA_2,5_7-G-5,08_1x07_P5.08mm_Horizontal', 'description': 'Generic Phoenix Contact connector footprint for: MSTBA_2,5/7-G-5,08; number of pins: 07; pin pitch: 5.08mm; Angled || order number: 1757297 12A || order number: 1923911 16A (HC)', 'tags': 'phoenix_contact connector MSTBA_01x07_G_5.08mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MSTB.3dshapes/PhoenixContact_MSTBA_2,5_7-G-5,08_1x07_P5.08mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_MSTB : PhoenixContact_MSTBA_2,5_7-G-5,08_1x07_P5.08mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

