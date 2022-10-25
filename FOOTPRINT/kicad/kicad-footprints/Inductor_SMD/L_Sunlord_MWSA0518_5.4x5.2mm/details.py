
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Sunlord_MWSA0518_5.4x5.2mm"
    hexID = "FZKINDUCTORSMLSUNLORDMWSA51854X52"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Sunlord_MWSA0518_5.4x5.2mm', 'description': 'Inductor, Sunlord, MWSA0518, 5.4mmx5.2mm', 'tags': 'inductor Sunlord smd', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Sunlord_MWSA0518.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Sunlord_MWSA0518_5.4x5.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

