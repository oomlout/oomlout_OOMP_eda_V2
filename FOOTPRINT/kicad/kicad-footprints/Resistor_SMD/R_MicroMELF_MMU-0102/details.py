
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_SMD"
    oIndex = "R_MicroMELF_MMU-0102"
    hexID = "FZKRESISTORSMRELFU12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_MicroMELF_MMU-0102', 'description': 'Resistor, MicroMELF, MMU-0102, http://www.vishay.com/docs/28713/melfprof.pdf', 'tags': 'MicroMELF Resistor', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_MicroMELF_MMU-0102.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Resistor_SMD : R_MicroMELF_MMU-0102')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

