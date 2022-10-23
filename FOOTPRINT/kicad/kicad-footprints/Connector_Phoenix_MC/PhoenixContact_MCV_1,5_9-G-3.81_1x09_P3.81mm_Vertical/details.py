
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MC"
    oIndex = "PhoenixContact_MCV_1,5_9-G-3.81_1x09_P3.81mm_Vertical"
    hexID = "FZKCNPHOENIXMCPHOENIXCONTACTMCV159G3811X9P381VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MCV_1,5_9-G-3.81_1x09_P3.81mm_Vertical', 'description': 'Generic Phoenix Contact connector footprint for: MCV_1,5/9-G-3.81; number of pins: 09; pin pitch: 3.81mm; Vertical || order number: 1803497 8A 160V', 'tags': 'phoenix_contact connector MCV_01x09_G_3.81mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MC.3dshapes/PhoenixContact_MCV_1,5_9-G-3.81_1x09_P3.81mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_MC : PhoenixContact_MCV_1,5_9-G-3.81_1x09_P3.81mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

