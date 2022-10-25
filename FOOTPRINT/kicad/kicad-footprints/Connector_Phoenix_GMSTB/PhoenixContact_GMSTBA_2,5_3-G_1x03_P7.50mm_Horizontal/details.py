
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_GMSTB"
    oIndex = "PhoenixContact_GMSTBA_2,5_3-G_1x03_P7.50mm_Horizontal"
    hexID = "FZKCNPHOENIXGMSTBPHOENIXCONTACTGMSTBA253G1X3P75HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_GMSTBA_2,5_3-G_1x03_P7.50mm_Horizontal', 'description': 'Generic Phoenix Contact connector footprint for: GMSTBA_2,5/3-G; number of pins: 03; pin pitch: 7.50mm; Angled || order number: 1766356 12A 630V', 'tags': 'phoenix_contact connector GMSTBA_01x03_G_7.50mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_GMSTB.3dshapes/PhoenixContact_GMSTBA_2,5_3-G_1x03_P7.50mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_GMSTB : PhoenixContact_GMSTBA_2,5_3-G_1x03_P7.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

