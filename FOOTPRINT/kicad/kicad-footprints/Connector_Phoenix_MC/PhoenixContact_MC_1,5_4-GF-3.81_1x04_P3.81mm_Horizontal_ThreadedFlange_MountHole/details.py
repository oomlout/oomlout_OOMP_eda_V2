
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MC"
    oIndex = "PhoenixContact_MC_1,5_4-GF-3.81_1x04_P3.81mm_Horizontal_ThreadedFlange_MountHole"
    hexID = "FZKCNPHOENIXMCPHOENIXCONTACTMC154GF3811X4P381HORIZONTALTHREADEDFLANGEMOUNTHOLE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MC_1,5_4-GF-3.81_1x04_P3.81mm_Horizontal_ThreadedFlange_MountHole', 'description': 'Generic Phoenix Contact connector footprint for: MC_1,5/4-GF-3.81; number of pins: 04; pin pitch: 3.81mm; Angled; threaded flange; footprint includes mount hole for mounting screw: ISO 1481-ST 2.2x4.5 C or ISO 7049-ST 2.2x4.5 C (http://www.fasteners.eu/standards/ISO/7049/) || order number: 1827884 8A 160V', 'tags': 'phoenix_contact connector MC_01x04_GF_3.81mm_MH', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MC.3dshapes/PhoenixContact_MC_1,5_4-GF-3.81_1x04_P3.81mm_Horizontal_ThreadedFlange_MountHole.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Phoenix_MC : PhoenixContact_MC_1,5_4-GF-3.81_1x04_P3.81mm_Horizontal_ThreadedFlange_MountHole')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

