
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MC"
    oIndex = "PhoenixContact_MC_1,5_13-G-3.81_1x13_P3.81mm_Horizontal"
    hexID = "FZKCNPHOENIXMCPHOENIXCONTACTMC1513G3811X13P381HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MC_1,5_13-G-3.81_1x13_P3.81mm_Horizontal', 'description': 'Generic Phoenix Contact connector footprint for: MC_1,5/13-G-3.81; number of pins: 13; pin pitch: 3.81mm; Angled || order number: 1803387 8A 160V', 'tags': 'phoenix_contact connector MC_01x13_G_3.81mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MC.3dshapes/PhoenixContact_MC_1,5_13-G-3.81_1x13_P3.81mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_MC : PhoenixContact_MC_1,5_13-G-3.81_1x13_P3.81mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

