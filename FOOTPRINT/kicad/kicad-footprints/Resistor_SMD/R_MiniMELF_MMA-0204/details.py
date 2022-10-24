
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_SMD"
    oIndex = "R_MiniMELF_MMA-0204"
    hexID = "FZKRESISTORSMRMMELFA24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_MiniMELF_MMA-0204', 'description': 'Resistor, MiniMELF, MMA-0204, http://www.vishay.com/docs/28713/melfprof.pdf', 'tags': 'MiniMELF Resistor', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_MiniMELF_MMA-0204.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Resistor_SMD : R_MiniMELF_MMA-0204')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

