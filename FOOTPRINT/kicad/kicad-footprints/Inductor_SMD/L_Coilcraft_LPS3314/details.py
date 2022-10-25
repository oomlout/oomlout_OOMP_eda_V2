
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Coilcraft_LPS3314"
    hexID = "FZKINDUCTORSMLCOILCRAFTLPS3314"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Coilcraft_LPS3314', 'description': 'SMD Inductor, 3.3x3.3x1.4mm, Coilcraft LPS3314, https://www.coilcraft.com/pdfs/lps3314.pdf', 'tags': 'L Coilcraft LPS3314', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Coilcraft_LPS3314.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Inductor_SMD : L_Coilcraft_LPS3314')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

