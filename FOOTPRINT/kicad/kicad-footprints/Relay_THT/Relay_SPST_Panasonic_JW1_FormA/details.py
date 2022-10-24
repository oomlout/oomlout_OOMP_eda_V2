
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_SPST_Panasonic_JW1_FormA"
    hexID = "FZKRELRELAYSPSTPANASONICJW1FORMA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_SPST_Panasonic_JW1_FormA', 'description': 'Panasonic Relay SPST, http://www3.panasonic.biz/ac/e_download/control/relay/power/catalog/mech_eng_jw.pdf?via=ok', 'tags': 'Panasonic Relay SPST', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_SPST_Panasonic_JW1_FormA.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Relay_THT : Relay_SPST_Panasonic_JW1_FormA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

