
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_GMSTB"
    oIndex = "PhoenixContact_GMSTBV_2,5_11-GF-7,62_1x11_P7.62mm_Vertical_ThreadedFlange"
    hexID = "FZKCNPHOENIXGMSTBPHOENIXCONTACTGMSTBV2511GF7621X11P762VERTICALTHREADEDFLANGE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_GMSTBV_2,5_11-GF-7,62_1x11_P7.62mm_Vertical_ThreadedFlange', 'description': 'Generic Phoenix Contact connector footprint for: GMSTBV_2,5/11-GF-7,62; number of pins: 11; pin pitch: 7.62mm; Vertical; threaded flange || order number: 1829248 12A 630V', 'tags': 'phoenix_contact connector GMSTBV_01x11_GF_7.62mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_GMSTB.3dshapes/PhoenixContact_GMSTBV_2,5_11-GF-7,62_1x11_P7.62mm_Vertical_ThreadedFlange.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_GMSTB : PhoenixContact_GMSTBV_2,5_11-GF-7,62_1x11_P7.62mm_Vertical_ThreadedFlange')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

