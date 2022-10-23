
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MC_HighVoltage"
    oIndex = "PhoenixContact_MC_1,5_3-GF-5.08_1x03_P5.08mm_Horizontal_ThreadedFlange"
    hexID = "FZKCNPHOENIXMCHIGHVOLTAGEPHOENIXCONTACTMC153GF581X3P58HORIZONTALTHREADEDFLANGE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MC_1,5_3-GF-5.08_1x03_P5.08mm_Horizontal_ThreadedFlange', 'description': 'Generic Phoenix Contact connector footprint for: MC_1,5/3-GF-5.08; number of pins: 03; pin pitch: 5.08mm; Angled; threaded flange || order number: 1847479 8A 320V', 'tags': 'phoenix_contact connector MC_01x03_GF_5.08mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MC_HighVoltage.3dshapes/PhoenixContact_MC_1,5_3-GF-5.08_1x03_P5.08mm_Horizontal_ThreadedFlange.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_MC_HighVoltage : PhoenixContact_MC_1,5_3-GF-5.08_1x03_P5.08mm_Horizontal_ThreadedFlange')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

