
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_GMSTB"
    oIndex = "PhoenixContact_GMSTBA_2,5_11-G-7,62_1x11_P7.62mm_Horizontal"
    hexID = "FZKCNPHOENIXGMSTBPHOENIXCONTACTGMSTBA2511G7621X11P762HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_GMSTBA_2,5_11-G-7,62_1x11_P7.62mm_Horizontal', 'description': 'Generic Phoenix Contact connector footprint for: GMSTBA_2,5/11-G-7,62; number of pins: 11; pin pitch: 7.62mm; Angled || order number: 1766327 12A 630V', 'tags': 'phoenix_contact connector GMSTBA_01x11_G_7.62mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_GMSTB.3dshapes/PhoenixContact_GMSTBA_2,5_11-G-7,62_1x11_P7.62mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_GMSTB : PhoenixContact_GMSTBA_2,5_11-G-7,62_1x11_P7.62mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

