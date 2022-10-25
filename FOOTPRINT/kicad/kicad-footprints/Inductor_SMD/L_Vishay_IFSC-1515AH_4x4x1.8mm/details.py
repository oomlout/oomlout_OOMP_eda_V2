
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Vishay_IFSC-1515AH_4x4x1.8mm"
    hexID = "FZKINDUCTORSMLVISHAYIFSC1515AH4X4X18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Vishay_IFSC-1515AH_4x4x1.8mm', 'description': 'Low Profile, High Current Inductors (https://www.vishay.com/docs/34295/sc15ah01.pdf)', 'tags': 'SMD Vishay Inductor Low Profile', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Vishay_IFSC-1515AH_4x4x1.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Vishay_IFSC-1515AH_4x4x1.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

