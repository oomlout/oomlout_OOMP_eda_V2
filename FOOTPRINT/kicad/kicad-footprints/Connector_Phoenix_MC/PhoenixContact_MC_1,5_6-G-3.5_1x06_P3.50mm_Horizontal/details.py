
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MC"
    oIndex = "PhoenixContact_MC_1,5_6-G-3.5_1x06_P3.50mm_Horizontal"
    hexID = "FZKCNPHOENIXMCPHOENIXCONTACTMC156G351X6P35HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MC_1,5_6-G-3.5_1x06_P3.50mm_Horizontal', 'description': 'Generic Phoenix Contact connector footprint for: MC_1,5/6-G-3.5; number of pins: 06; pin pitch: 3.50mm; Angled || order number: 1844252 8A 160V', 'tags': 'phoenix_contact connector MC_01x06_G_3.5mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MC.3dshapes/PhoenixContact_MC_1,5_6-G-3.5_1x06_P3.50mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_MC : PhoenixContact_MC_1,5_6-G-3.5_1x06_P3.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

