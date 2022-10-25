
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_Abracon_ASDMB-4Pin_2.5x2.0mm"
    hexID = "FZKOCSOCSSMABRACONASDMB4PIN25X2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_Abracon_ASDMB-4Pin_2.5x2.0mm', 'description': 'Miniature Crystal Clock Oscillator Abracon ASDMB series, 2.5x2.0mm package, http://www.abracon.com/Oscillators/ASDMB.pdf', 'tags': 'SMD SMT crystal oscillator', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_Abracon_ASDMB-4Pin_2.5x2.0mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_Abracon_ASDMB-4Pin_2.5x2.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

