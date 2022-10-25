
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "TRNN-SO23-X-KS8050-01-TN98050"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSTRNNSO23XKS851TN985"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TRNN-SO23-X-KS8050-01-TN98050', 'description': 'hexID: TN98050; SOT, 3 Pin (https://www.jedec.org/system/files/docs/to-236h.pdf variant AB), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SOT TO_SOT_SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/SOT-23.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('oomlout_OOMP_parts : TRNN-SO23-X-KS8050-01-TN98050')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

