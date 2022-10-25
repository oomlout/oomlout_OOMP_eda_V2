
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Abracon_ASPI-4030S"
    hexID = "FZKINDUCTORSMLABRACONASPI43S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Abracon_ASPI-4030S', 'description': 'smd shielded power inductor 4x4x3mm, Abracon ASPI-4030S, https://abracon.com/Magnetics/power/ASPI-4030S.pdf', 'tags': 'inductor abracon smd shielded', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Abracon_ASPI-4030S.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Inductor_SMD : L_Abracon_ASPI-4030S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

