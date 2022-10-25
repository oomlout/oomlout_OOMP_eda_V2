
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "ST_UFQFPN-20_3x3mm_P0.5mm"
    hexID = "FZKDFNSTUFQFPN23X3P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ST_UFQFPN-20_3x3mm_P0.5mm', 'description': 'UFQFPN 20-lead, 3 x 3 mm, 0.5 mm pitch, ultra thin fine pitch quad flat package (http://www.st.com/resource/en/datasheet/stm8s003f3.pdf)', 'tags': 'UFQFPN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/ST_UFQFPN-20_3x3mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Package_DFN_QFN : ST_UFQFPN-20_3x3mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

