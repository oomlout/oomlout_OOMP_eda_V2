
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "MOSN-T252-X-K4184-01-MN2524184A"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSMOSNT252XK41841MN2524184A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MOSN-T252-X-K4184-01-MN2524184A', 'description': 'hexID: MN2524184A; TO-252 / DPAK SMD package, http://www.infineon.com/cms/en/product/packages/PG-TO252/PG-TO252-3-1/', 'tags': 'DPAK TO-252 DPAK-3 TO-252-3 SOT-428', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/TO-252-3_TabPin2.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('oomlout_OOMP_parts : MOSN-T252-X-K4184-01-MN2524184A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

