
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_SMD"
    oIndex = "R_Shunt_Ohmite_LVK24"
    hexID = "FZKRESISTORSMRSHUNTOHMITELVK24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Shunt_Ohmite_LVK24', 'description': '4 contacts shunt resistor,https://www.ohmite.com/assets/docs/res_lvk.pdf', 'tags': '4 contacts resistor smd', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_Shunt_Ohmite_LVK24.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Resistor_SMD : R_Shunt_Ohmite_LVK24')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

