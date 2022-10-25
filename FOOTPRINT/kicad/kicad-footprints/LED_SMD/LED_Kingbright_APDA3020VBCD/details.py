
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_Kingbright_APDA3020VBCD"
    hexID = "FZKLSMLKINGBRIGHTAPDA32VBCD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_Kingbright_APDA3020VBCD', 'description': 'LED, SMD, APDA3020VBC/D, https://www.kingbrightusa.com/images/catalog/SPEC/APDA3020VBC-D.pdf', 'tags': 'LED APDA3020VBC/D Kingbright ', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Kingbright_APDA3020VBCD.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('LED_SMD : LED_Kingbright_APDA3020VBCD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

