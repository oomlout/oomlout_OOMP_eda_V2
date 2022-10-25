
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MC_HighVoltage"
    oIndex = "PhoenixContact_MC_1,5_8-GF-5.08_1x08_P5.08mm_Horizontal_ThreadedFlange_MountHole"
    hexID = "FZKCNPHOENIXMCHIGHVOLTAGEPHOENIXCONTACTMC158GF581X8P58HORIZONTALTHREADEDFLANGEMOUNTHOLE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MC_1,5_8-GF-5.08_1x08_P5.08mm_Horizontal_ThreadedFlange_MountHole', 'description': 'Generic Phoenix Contact connector footprint for: MC_1,5/8-GF-5.08; number of pins: 08; pin pitch: 5.08mm; Angled; threaded flange; footprint includes mount hole for mounting screw: ISO 1481-ST 2.2x4.5 C or ISO 7049-ST 2.2x4.5 C (http://www.fasteners.eu/standards/ISO/7049/) || order number: 1847521 8A 320V', 'tags': 'phoenix_contact connector MC_01x08_GF_5.08mm_MH', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MC_HighVoltage.3dshapes/PhoenixContact_MC_1,5_8-GF-5.08_1x08_P5.08mm_Horizontal_ThreadedFlange_MountHole.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Phoenix_MC_HighVoltage : PhoenixContact_MC_1,5_8-GF-5.08_1x08_P5.08mm_Horizontal_ThreadedFlange_MountHole')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

