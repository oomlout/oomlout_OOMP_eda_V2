
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_GMSTB"
    oIndex = "PhoenixContact_GMSTBVA_2,5_12-G-7,62_1x12_P7.62mm_Vertical"
    hexID = "FZKCNPHOENIXGMSTBPHOENIXCONTACTGMSTBVA2512G7621X12P762VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_GMSTBVA_2,5_12-G-7,62_1x12_P7.62mm_Vertical', 'description': 'Generic Phoenix Contact connector footprint for: GMSTBVA_2,5/12-G-7,62; number of pins: 12; pin pitch: 7.62mm; Vertical || order number: 1766877 12A 630V', 'tags': 'phoenix_contact connector GMSTBVA_01x12_G_7.62mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_GMSTB.3dshapes/PhoenixContact_GMSTBVA_2,5_12-G-7,62_1x12_P7.62mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_GMSTB : PhoenixContact_GMSTBVA_2,5_12-G-7,62_1x12_P7.62mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

