
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_Abracon_ASV-4Pin_7.0x5.1mm_HandSoldering"
    hexID = "FZKOCSOCSSMABRACONASV4PIN7X51HANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_Abracon_ASV-4Pin_7.0x5.1mm_HandSoldering', 'description': 'Miniature Crystal Clock Oscillator Abracon ASV series, http://www.abracon.com/Oscillators/ASV.pdf, hand-soldering, 7.0x5.1mm^2 package', 'tags': 'SMD SMT crystal oscillator hand-soldering', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_Abracon_ASV-4Pin_7.0x5.1mm_HandSoldering.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_Abracon_ASV-4Pin_7.0x5.1mm_HandSoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

