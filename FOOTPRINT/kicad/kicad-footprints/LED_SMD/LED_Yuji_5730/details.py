
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_Yuji_5730"
    hexID = "FZKLSMLYUJI573"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_Yuji_5730', 'description': 'LED,Yuji,5730,https://cdn.shopify.com/s/files/1/0344/6401/files/YJWJ014-1.1_YJ-BC-5730L-G02.pdf', 'tags': 'LED Yuji 5730', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Yuji_5730.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_Yuji_5730')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

