
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "Panasonic_EVQPUL_EVQPUC"
    hexID = "FZKBSWITCHSMPEVQPULEVQPUC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Panasonic_EVQPUL_EVQPUC', 'description': 'http://industrial.panasonic.com/cdbs/www-data/pdf/ATV0000/ATV0000CE5.pdf', 'tags': 'SMD SMT SPST EVQPUL EVQPUC', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/Panasonic_EVQPUL_EVQPUC.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Button_Switch_SMD : Panasonic_EVQPUL_EVQPUC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

