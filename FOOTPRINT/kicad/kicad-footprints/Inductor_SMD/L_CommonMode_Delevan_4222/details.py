
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_CommonMode_Delevan_4222"
    hexID = "FZKINDUCTORSMLCOONMODEDELEVAN4222"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_CommonMode_Delevan_4222', 'description': 'API Delevan, Surface Mount Common Mode Bead, 4222 4222R, http://www.delevan.com/seriesPDFs/4222.pdf', 'tags': 'surface mount common mode bead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_CommonMode_Delevan_4222.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_CommonMode_Delevan_4222')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

