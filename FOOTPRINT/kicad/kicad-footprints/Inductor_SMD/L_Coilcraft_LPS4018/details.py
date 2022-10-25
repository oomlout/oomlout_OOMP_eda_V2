
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Coilcraft_LPS4018"
    hexID = "FZKINDUCTORSMLCOILCRAFTLPS418"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Coilcraft_LPS4018', 'description': 'SMD Inductor Coilcraft LPS4018 https://www.coilcraft.com/pdfs/lps4018.pdf', 'tags': 'L Coilcraft LPS4018', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Coilcraft_LPS4018.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Inductor_SMD : L_Coilcraft_LPS4018')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

