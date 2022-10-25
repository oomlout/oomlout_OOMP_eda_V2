
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_Kingbright_AAA3528ESGCT"
    hexID = "FZKLSMLKINGBRIGHTAAA3528ESGCT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_Kingbright_AAA3528ESGCT', 'description': 'Kingbright, dual LED, 3.5 x 2.8 mm Surface Mount LED Lamp (http://www.kingbrightusa.com/images/catalog/SPEC/AAA3528ESGCT.pdf)', 'tags': 'dual led smd', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Kingbright_AAA3528ESGCT.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_Kingbright_AAA3528ESGCT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

