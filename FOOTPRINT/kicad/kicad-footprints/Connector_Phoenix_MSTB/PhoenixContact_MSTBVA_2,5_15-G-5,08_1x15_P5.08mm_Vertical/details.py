
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MSTB"
    oIndex = "PhoenixContact_MSTBVA_2,5_15-G-5,08_1x15_P5.08mm_Vertical"
    hexID = "FZKCNPHOENIXMSTBPHOENIXCONTACTMSTBVA2515G581X15P58VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MSTBVA_2,5_15-G-5,08_1x15_P5.08mm_Vertical', 'description': 'Generic Phoenix Contact connector footprint for: MSTBVA_2,5/15-G-5,08; number of pins: 15; pin pitch: 5.08mm; Vertical || order number: 1755862 12A', 'tags': 'phoenix_contact connector MSTBVA_01x15_G_5.08mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MSTB.3dshapes/PhoenixContact_MSTBVA_2,5_15-G-5,08_1x15_P5.08mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_MSTB : PhoenixContact_MSTBVA_2,5_15-G-5,08_1x15_P5.08mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

