
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MSTB"
    oIndex = "PhoenixContact_MSTB_2,5_10-GF_1x10_P5.00mm_Horizontal_ThreadedFlange"
    hexID = "FZKCNPHOENIXMSTBPHOENIXCONTACTMSTB251GF1X1P5HORIZONTALTHREADEDFLANGE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MSTB_2,5_10-GF_1x10_P5.00mm_Horizontal_ThreadedFlange', 'description': 'Generic Phoenix Contact connector footprint for: MSTB_2,5/10-GF; number of pins: 10; pin pitch: 5.00mm; Angled; threaded flange || order number: 1776773 12A || order number: 1924059 16A (HC)', 'tags': 'phoenix_contact connector MSTB_01x10_GF_5.00mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MSTB.3dshapes/PhoenixContact_MSTB_2,5_10-GF_1x10_P5.00mm_Horizontal_ThreadedFlange.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_MSTB : PhoenixContact_MSTB_2,5_10-GF_1x10_P5.00mm_Horizontal_ThreadedFlange')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

