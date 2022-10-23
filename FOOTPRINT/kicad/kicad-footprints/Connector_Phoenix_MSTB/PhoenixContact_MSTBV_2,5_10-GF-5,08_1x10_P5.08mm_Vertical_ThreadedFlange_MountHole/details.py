
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MSTB"
    oIndex = "PhoenixContact_MSTBV_2,5_10-GF-5,08_1x10_P5.08mm_Vertical_ThreadedFlange_MountHole"
    hexID = "FZKCNPHOENIXMSTBPHOENIXCONTACTMSTBV251GF581X1P58VERTICALTHREADEDFLANGEMOUNTHOLE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MSTBV_2,5_10-GF-5,08_1x10_P5.08mm_Vertical_ThreadedFlange_MountHole', 'description': 'Generic Phoenix Contact connector footprint for: MSTBV_2,5/10-GF-5,08; number of pins: 10; pin pitch: 5.08mm; Vertical; threaded flange; footprint includes mount hole for mounting screw: ISO 1481-ST 2.2x6.5 C or ISO 7049-ST 2.2x6.5 C (http://www.fasteners.eu/standards/ISO/7049/) || order number: 1777154 12A || order number: 1924606 16A (HC)', 'tags': 'phoenix_contact connector MSTBV_01x10_GF_5.08mm_MH', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MSTB.3dshapes/PhoenixContact_MSTBV_2,5_10-GF-5,08_1x10_P5.08mm_Vertical_ThreadedFlange_MountHole.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Phoenix_MSTB : PhoenixContact_MSTBV_2,5_10-GF-5,08_1x10_P5.08mm_Vertical_ThreadedFlange_MountHole')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

