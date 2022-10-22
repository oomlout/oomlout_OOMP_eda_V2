
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "VREG-SO235-X-KAP2112K-V33D-V235AP2112K33"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSVREGSO235XKAP2112KV33DV235AP2112K33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VREG-SO235-X-KAP2112K-V33D-V235AP2112K33', 'description': 'hexID: V235AP2112K33; SOT, 5 Pin (https://www.jedec.org/sites/default/files/docs/Mo-178c.PDF variant AA), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SOT TO_SOT_SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/SOT-23-5.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('oomlout_OOMP_parts : VREG-SO235-X-KAP2112K-V33D-V235AP2112K33')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

