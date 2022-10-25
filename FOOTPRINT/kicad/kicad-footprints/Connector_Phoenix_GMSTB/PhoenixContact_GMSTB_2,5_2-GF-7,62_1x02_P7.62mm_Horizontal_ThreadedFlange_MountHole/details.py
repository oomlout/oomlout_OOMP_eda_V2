
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_GMSTB"
    oIndex = "PhoenixContact_GMSTB_2,5_2-GF-7,62_1x02_P7.62mm_Horizontal_ThreadedFlange_MountHole"
    hexID = "FZKCNPHOENIXGMSTBPHOENIXCONTACTGMSTB252GF7621X2P762HORIZONTALTHREADEDFLANGEMOUNTHOLE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_GMSTB_2,5_2-GF-7,62_1x02_P7.62mm_Horizontal_ThreadedFlange_MountHole', 'description': 'Generic Phoenix Contact connector footprint for: GMSTB_2,5/2-GF-7,62; number of pins: 02; pin pitch: 7.62mm; Angled; threaded flange; footprint includes mount hole for mounting screw: ISO 1481-ST 2.2x6.5 C or ISO 7049-ST 2.2x6.5 C (http://www.fasteners.eu/standards/ISO/7049/) || order number: 1806229 12A 630V', 'tags': 'phoenix_contact connector GMSTB_01x02_GF_7.62mm_MH', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_GMSTB.3dshapes/PhoenixContact_GMSTB_2,5_2-GF-7,62_1x02_P7.62mm_Horizontal_ThreadedFlange_MountHole.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Phoenix_GMSTB : PhoenixContact_GMSTB_2,5_2-GF-7,62_1x02_P7.62mm_Horizontal_ThreadedFlange_MountHole')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

