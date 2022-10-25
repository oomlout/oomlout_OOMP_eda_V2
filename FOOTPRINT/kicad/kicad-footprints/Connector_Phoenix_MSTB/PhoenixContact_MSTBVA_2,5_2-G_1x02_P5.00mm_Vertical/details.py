
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MSTB"
    oIndex = "PhoenixContact_MSTBVA_2,5_2-G_1x02_P5.00mm_Vertical"
    hexID = "FZKCNPHOENIXMSTBPHOENIXCONTACTMSTBVA252G1X2P5VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MSTBVA_2,5_2-G_1x02_P5.00mm_Vertical', 'description': 'Generic Phoenix Contact connector footprint for: MSTBVA_2,5/2-G; number of pins: 02; pin pitch: 5.00mm; Vertical || order number: 1755516 12A || order number: 1924198 16A (HC)', 'tags': 'phoenix_contact connector MSTBVA_01x02_G_5.00mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MSTB.3dshapes/PhoenixContact_MSTBVA_2,5_2-G_1x02_P5.00mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_MSTB : PhoenixContact_MSTBVA_2,5_2-G_1x02_P5.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

