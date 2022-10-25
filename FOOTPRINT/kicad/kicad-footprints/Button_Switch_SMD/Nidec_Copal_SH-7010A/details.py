
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "Nidec_Copal_SH-7010A"
    hexID = "FZKBSWITCHSMNIDECCOPALSH71A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Nidec_Copal_SH-7010A', 'description': '4-bit rotary coded switch, J-hook, https://www.nidec-copal-electronics.com/e/catalog/switch/sh-7000.pdf', 'tags': 'rotary switch bcd', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/Nidec_Copal_SH-7010A.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : Nidec_Copal_SH-7010A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

