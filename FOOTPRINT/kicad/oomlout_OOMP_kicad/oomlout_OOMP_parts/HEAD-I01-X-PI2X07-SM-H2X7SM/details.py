
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "HEAD-I01-X-PI2X07-SM-H2X7SM"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSHEADI1XPI2X7SMH2X7SM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HEAD-I01-X-PI2X07-SM-H2X7SM', 'description': 'hexID: H2X7SM; surface-mounted straight pin header, 2x07, 2.54mm pitch, double rows', 'tags': 'Surface mounted pin header SMD 2x07 2.54mm double row', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinHeader_2.54mm.3dshapes/PinHeader_2x07_P2.54mm_Vertical_SMD.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('oomlout_OOMP_parts : HEAD-I01-X-PI2X07-SM-H2X7SM')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

