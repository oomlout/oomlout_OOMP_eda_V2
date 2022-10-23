
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_GMSTB"
    oIndex = "PhoenixContact_GMSTBVA_2,5_10-G-7,62_1x10_P7.62mm_Vertical"
    hexID = "FZKCNPHOENIXGMSTBPHOENIXCONTACTGMSTBVA251G7621X1P762VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_GMSTBVA_2,5_10-G-7,62_1x10_P7.62mm_Vertical', 'description': 'Generic Phoenix Contact connector footprint for: GMSTBVA_2,5/10-G-7,62; number of pins: 10; pin pitch: 7.62mm; Vertical || order number: 1766851 12A 630V', 'tags': 'phoenix_contact connector GMSTBVA_01x10_G_7.62mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_GMSTB.3dshapes/PhoenixContact_GMSTBVA_2,5_10-G-7,62_1x10_P7.62mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_GMSTB : PhoenixContact_GMSTBVA_2,5_10-G-7,62_1x10_P7.62mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

