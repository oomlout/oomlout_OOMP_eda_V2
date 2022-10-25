
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Vishay_IHSM-3825"
    hexID = "FZKINDUCTORSMLVISHAYIHSM3825"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Vishay_IHSM-3825', 'description': 'Inductor, Vishay, Vishay_IHSM-3825, http://www.vishay.com/docs/34018/ihsm3825.pdf, 11.2mmx6.3mm', 'tags': 'inductor vishay icsm smd', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Vishay_IHSM-3825.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Vishay_IHSM-3825')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

