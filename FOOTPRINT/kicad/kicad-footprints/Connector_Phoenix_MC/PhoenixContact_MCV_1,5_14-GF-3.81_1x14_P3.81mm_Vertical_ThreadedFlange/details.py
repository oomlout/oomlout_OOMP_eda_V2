
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MC"
    oIndex = "PhoenixContact_MCV_1,5_14-GF-3.81_1x14_P3.81mm_Vertical_ThreadedFlange"
    hexID = "FZKCNPHOENIXMCPHOENIXCONTACTMCV1514GF3811X14P381VERTICALTHREADEDFLANGE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MCV_1,5_14-GF-3.81_1x14_P3.81mm_Vertical_ThreadedFlange', 'description': 'Generic Phoenix Contact connector footprint for: MCV_1,5/14-GF-3.81; number of pins: 14; pin pitch: 3.81mm; Vertical; threaded flange || order number: 1830716 8A 160V', 'tags': 'phoenix_contact connector MCV_01x14_GF_3.81mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MC.3dshapes/PhoenixContact_MCV_1,5_14-GF-3.81_1x14_P3.81mm_Vertical_ThreadedFlange.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_MC : PhoenixContact_MCV_1,5_14-GF-3.81_1x14_P3.81mm_Vertical_ThreadedFlange')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

