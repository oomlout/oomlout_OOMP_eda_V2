
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Phoenix_MSTB"
    oIndex = "PhoenixContact_MSTB_2,5_9-GF_1x09_P5.00mm_Horizontal_ThreadedFlange_MountHole"
    hexID = "FZKCNPHOENIXMSTBPHOENIXCONTACTMSTB259GF1X9P5HORIZONTALTHREADEDFLANGEMOUNTHOLE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PhoenixContact_MSTB_2,5_9-GF_1x09_P5.00mm_Horizontal_ThreadedFlange_MountHole', 'description': 'Generic Phoenix Contact connector footprint for: MSTB_2,5/9-GF; number of pins: 09; pin pitch: 5.00mm; Angled; threaded flange; footprint includes mount hole for mounting screw: ISO 1481-ST 2.2x6.5 C or ISO 7049-ST 2.2x6.5 C (http://www.fasteners.eu/standards/ISO/7049/) || order number: 1776760 12A || order number: 1924046 16A (HC)', 'tags': 'phoenix_contact connector MSTB_01x09_GF_5.00mm_MH', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Phoenix_MSTB.3dshapes/PhoenixContact_MSTB_2,5_9-GF_1x09_P5.00mm_Horizontal_ThreadedFlange_MountHole.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Phoenix_MSTB : PhoenixContact_MSTB_2,5_9-GF_1x09_P5.00mm_Horizontal_ThreadedFlange_MountHole')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

