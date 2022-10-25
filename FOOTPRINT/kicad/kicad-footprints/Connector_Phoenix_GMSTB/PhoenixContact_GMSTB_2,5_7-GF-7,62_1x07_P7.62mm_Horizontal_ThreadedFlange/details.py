
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_GMSTB"
    oIndex = "PhoenixContact_GMSTB_2,5_7-GF-7,62_1x07_P7.62mm_Horizontal_ThreadedFlange"
    hexID = "FZKCNPHOENIXGMSTBPHOENIXCONTACTGMSTB257GF7621X7P762HORIZONTALTHREADEDFLANGE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_GMSTB_2,5_7-GF-7,62_1x07_P7.62mm_Horizontal_ThreadedFlange', 'description': 'Generic Phoenix Contact connector footprint for: GMSTB_2,5/7-GF-7,62; number of pins: 07; pin pitch: 7.62mm; Angled; threaded flange || order number: 1806274 12A 630V', 'tags': 'phoenix_contact connector GMSTB_01x07_GF_7.62mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_GMSTB.3dshapes/PhoenixContact_GMSTB_2,5_7-GF-7,62_1x07_P7.62mm_Horizontal_ThreadedFlange.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_GMSTB : PhoenixContact_GMSTB_2,5_7-GF-7,62_1x07_P7.62mm_Horizontal_ThreadedFlange')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

