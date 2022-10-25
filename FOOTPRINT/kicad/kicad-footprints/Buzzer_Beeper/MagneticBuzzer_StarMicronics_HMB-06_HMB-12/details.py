
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Buzzer_Beeper"
    oIndex = "MagneticBuzzer_StarMicronics_HMB-06_HMB-12"
    hexID = "FZKBZMAGNETICBUZZERSTARMNICSHMB6HMB12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MagneticBuzzer_StarMicronics_HMB-06_HMB-12', 'description': 'Buzzer, Elektromagnetic Beeper, Summer,', 'tags': 'Star Micronics HMB-06 HMB-12', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Buzzer_Beeper.3dshapes/MagneticBuzzer_StarMicronics_HMB-06_HMB-12.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Buzzer_Beeper : MagneticBuzzer_StarMicronics_HMB-06_HMB-12')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

