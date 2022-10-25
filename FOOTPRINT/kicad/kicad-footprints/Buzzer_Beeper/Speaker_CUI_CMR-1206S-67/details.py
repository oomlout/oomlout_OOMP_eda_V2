
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Buzzer_Beeper"
    oIndex = "Speaker_CUI_CMR-1206S-67"
    hexID = "FZKBZSPEAKERCUICMR126S67"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Speaker_CUI_CMR-1206S-67', 'description': 'Speaker, 30mW, 300-7000Hz, IP67 face, 12x6x2,25mm, https://www.cuidevices.com/product/resource/cmr-12062s-67.pdf', 'tags': 'speaker CUI', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Buzzer_Beeper.3dshapes/Speaker_CUI_CMR-1206S-67.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Buzzer_Beeper : Speaker_CUI_CMR-1206S-67')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

