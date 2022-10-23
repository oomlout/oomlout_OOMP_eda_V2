
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MC_HighVoltage"
    oIndex = "PhoenixContact_MC_1,5_4-G-5.08_1x04_P5.08mm_Horizontal"
    hexID = "FZKCNPHOENIXMCHIGHVOLTAGEPHOENIXCONTACTMC154G581X4P58HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MC_1,5_4-G-5.08_1x04_P5.08mm_Horizontal', 'description': 'Generic Phoenix Contact connector footprint for: MC_1,5/4-G-5.08; number of pins: 04; pin pitch: 5.08mm; Angled || order number: 1836202 8A 320V', 'tags': 'phoenix_contact connector MC_01x04_G_5.08mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MC_HighVoltage.3dshapes/PhoenixContact_MC_1,5_4-G-5.08_1x04_P5.08mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_MC_HighVoltage : PhoenixContact_MC_1,5_4-G-5.08_1x04_P5.08mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

