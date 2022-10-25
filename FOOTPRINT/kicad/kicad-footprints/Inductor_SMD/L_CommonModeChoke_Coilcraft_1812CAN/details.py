
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_CommonModeChoke_Coilcraft_1812CAN"
    hexID = "FZKINDUCTORSMLCOONMODECHOKECOILCRAFT1812CAN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_CommonModeChoke_Coilcraft_1812CAN', 'description': 'Coilcraft 1812CAN Series Common Mode Choke, https://www.coilcraft.com/pdfs/1812can.pdf', 'tags': 'surface mount common mode bead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_CommonModeChoke_Coilcraft_1812CAN.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Inductor_SMD : L_CommonModeChoke_Coilcraft_1812CAN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

