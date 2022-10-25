
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_GMSTB"
    oIndex = "PhoenixContact_GMSTBVA_2,5_6-G_1x06_P7.50mm_Vertical"
    hexID = "FZKCNPHOENIXGMSTBPHOENIXCONTACTGMSTBVA256G1X6P75VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_GMSTBVA_2,5_6-G_1x06_P7.50mm_Vertical', 'description': 'Generic Phoenix Contact connector footprint for: GMSTBVA_2,5/6-G; number of pins: 06; pin pitch: 7.50mm; Vertical || order number: 1766709 12A 630V', 'tags': 'phoenix_contact connector GMSTBVA_01x06_G_7.50mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_GMSTB.3dshapes/PhoenixContact_GMSTBVA_2,5_6-G_1x06_P7.50mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_GMSTB : PhoenixContact_GMSTBVA_2,5_6-G_1x06_P7.50mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

