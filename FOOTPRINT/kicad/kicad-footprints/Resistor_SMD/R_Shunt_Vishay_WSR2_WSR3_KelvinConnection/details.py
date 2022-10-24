
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_SMD"
    oIndex = "R_Shunt_Vishay_WSR2_WSR3_KelvinConnection"
    hexID = "FZKRESISTORSMRSHUNTVISHAYWSR2WSR3KELVINCONNECTION"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Shunt_Vishay_WSR2_WSR3_KelvinConnection', 'description': 'Power Metal Strip Resistors 0.005 to 0.2, https://www.vishay.com/docs/30101/wsr.pdf', 'tags': 'SMD Shunt Resistor', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_Shunt_Vishay_WSR2_WSR3.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Resistor_SMD : R_Shunt_Vishay_WSR2_WSR3_KelvinConnection')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

