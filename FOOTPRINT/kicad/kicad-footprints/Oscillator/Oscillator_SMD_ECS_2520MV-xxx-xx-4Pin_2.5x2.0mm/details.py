
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_ECS_2520MV-xxx-xx-4Pin_2.5x2.0mm"
    hexID = "FZKOCSOCSSMECS252MVXXXXX4PIN25X2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_ECS_2520MV-xxx-xx-4Pin_2.5x2.0mm', 'description': 'Miniature Crystal Clock Oscillator ECS 2520MV series, https://www.ecsxtal.com/store/pdf/ECS-2520MV.pdf', 'tags': 'Miniature Crystal Clock Oscillator ECS 2520MV series SMD SMT HCMOS', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_ECS_2520MV-xxx-xx-4Pin_2.5x2.0mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_ECS_2520MV-xxx-xx-4Pin_2.5x2.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

