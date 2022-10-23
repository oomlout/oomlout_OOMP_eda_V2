
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MC_HighVoltage"
    oIndex = "PhoenixContact_MCV_1,5_5-GF-5.08_1x05_P5.08mm_Vertical_ThreadedFlange"
    hexID = "FZKCNPHOENIXMCHIGHVOLTAGEPHOENIXCONTACTMCV155GF581X5P58VERTICALTHREADEDFLANGE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MCV_1,5_5-GF-5.08_1x05_P5.08mm_Vertical_ThreadedFlange', 'description': 'Generic Phoenix Contact connector footprint for: MCV_1,5/5-GF-5.08; number of pins: 05; pin pitch: 5.08mm; Vertical; threaded flange || order number: 1847644 8A 320V', 'tags': 'phoenix_contact connector MCV_01x05_GF_5.08mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MC_HighVoltage.3dshapes/PhoenixContact_MCV_1,5_5-GF-5.08_1x05_P5.08mm_Vertical_ThreadedFlange.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Phoenix_MC_HighVoltage : PhoenixContact_MCV_1,5_5-GF-5.08_1x05_P5.08mm_Vertical_ThreadedFlange')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

