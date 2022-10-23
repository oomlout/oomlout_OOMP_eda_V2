
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MC"
    oIndex = "PhoenixContact_MCV_1,5_14-GF-3.5_1x14_P3.50mm_Vertical_ThreadedFlange_MountHole"
    hexID = "FZKCNPHOENIXMCPHOENIXCONTACTMCV1514GF351X14P35VERTICALTHREADEDFLANGEMOUNTHOLE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MCV_1,5_14-GF-3.5_1x14_P3.50mm_Vertical_ThreadedFlange_MountHole', 'description': 'Generic Phoenix Contact connector footprint for: MCV_1,5/14-GF-3.5; number of pins: 14; pin pitch: 3.50mm; Vertical; threaded flange; footprint includes mount hole for mounting screw: ISO 1481-ST 2.2x4.5 C or ISO 7049-ST 2.2x4.5 C (http://www.fasteners.eu/standards/ISO/7049/) || order number: 1843347 8A 160V', 'tags': 'phoenix_contact connector MCV_01x14_GF_3.5mm_MH', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MC.3dshapes/PhoenixContact_MCV_1,5_14-GF-3.5_1x14_P3.50mm_Vertical_ThreadedFlange_MountHole.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Phoenix_MC : PhoenixContact_MCV_1,5_14-GF-3.5_1x14_P3.50mm_Vertical_ThreadedFlange_MountHole')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

