
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MSTB"
    oIndex = "PhoenixContact_MSTBV_2,5_7-GF-5,08_1x07_P5.08mm_Vertical_ThreadedFlange"
    hexID = "FZKCNPHOENIXMSTBPHOENIXCONTACTMSTBV257GF581X7P58VERTICALTHREADEDFLANGE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MSTBV_2,5_7-GF-5,08_1x07_P5.08mm_Vertical_ThreadedFlange', 'description': 'Generic Phoenix Contact connector footprint for: MSTBV_2,5/7-GF-5,08; number of pins: 07; pin pitch: 5.08mm; Vertical; threaded flange || order number: 1777125 12A || order number: 1924570 16A (HC)', 'tags': 'phoenix_contact connector MSTBV_01x07_GF_5.08mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MSTB.3dshapes/PhoenixContact_MSTBV_2,5_7-GF-5,08_1x07_P5.08mm_Vertical_ThreadedFlange.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_MSTB : PhoenixContact_MSTBV_2,5_7-GF-5,08_1x07_P5.08mm_Vertical_ThreadedFlange')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

