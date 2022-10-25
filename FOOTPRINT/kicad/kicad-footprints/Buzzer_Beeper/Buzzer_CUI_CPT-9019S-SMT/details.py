
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Buzzer_Beeper"
    oIndex = "Buzzer_CUI_CPT-9019S-SMT"
    hexID = "FZKBZBUZZERCUICPT919SS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Buzzer_CUI_CPT-9019S-SMT', 'description': 'https://www.cui.com/product/resource/cpt-9019s-smt.pdf', 'tags': 'buzzer piezo', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Buzzer_Beeper.3dshapes/Buzzer_CUI_CPT-9019S-SMT.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Buzzer_Beeper : Buzzer_CUI_CPT-9019S-SMT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

