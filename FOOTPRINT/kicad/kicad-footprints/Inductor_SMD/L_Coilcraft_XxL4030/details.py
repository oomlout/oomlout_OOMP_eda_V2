
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Coilcraft_XxL4030"
    hexID = "FZKINDUCTORSMLCOILCRAFTXXL43"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Coilcraft_XxL4030', 'description': 'L_Coilcraft_XxL4030 https://www.coilcraft.com/pdfs/xfl4030.pdf', 'tags': 'L Coilcraft XxL4030', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Coilcraft_XxL4030.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Coilcraft_XxL4030')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

