
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Pulse_PA4320"
    hexID = "FZKINDUCTORSMLPULSEPA432"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Pulse_PA4320', 'description': 'Inductor SMD Pulse PA4320 http://productfinder.pulseeng.com/products/datasheets/P787.pdf', 'tags': 'Inductor SMD Pulse PA4320', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Pulse_PA4320.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Pulse_PA4320')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

