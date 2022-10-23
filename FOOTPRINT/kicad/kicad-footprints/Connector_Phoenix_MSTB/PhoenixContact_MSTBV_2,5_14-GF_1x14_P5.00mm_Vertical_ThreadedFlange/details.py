
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MSTB"
    oIndex = "PhoenixContact_MSTBV_2,5_14-GF_1x14_P5.00mm_Vertical_ThreadedFlange"
    hexID = "FZKCNPHOENIXMSTBPHOENIXCONTACTMSTBV2514GF1X14P5VERTICALTHREADEDFLANGE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MSTBV_2,5_14-GF_1x14_P5.00mm_Vertical_ThreadedFlange', 'description': 'Generic Phoenix Contact connector footprint for: MSTBV_2,5/14-GF; number of pins: 14; pin pitch: 5.00mm; Vertical; threaded flange || order number: 1776002 12A', 'tags': 'phoenix_contact connector MSTBV_01x14_GF_5.00mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MSTB.3dshapes/PhoenixContact_MSTBV_2,5_14-GF_1x14_P5.00mm_Vertical_ThreadedFlange.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_MSTB : PhoenixContact_MSTBV_2,5_14-GF_1x14_P5.00mm_Vertical_ThreadedFlange')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

