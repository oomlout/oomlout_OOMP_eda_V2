
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_Push_1P1T_NO_CK_KSC6xxJ"
    hexID = "FZKBSWITCHSMSWPUSH1P1TNOCKKSC6XXJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_Push_1P1T_NO_CK_KSC6xxJ', 'description': 'CK components KSC6 tactile switch https://www.ckswitches.com/media/1972/ksc6.pdf', 'tags': 'tactile switch ksc6', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_push_1P1T_NO_CK_KSC6xxJxxx.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_Push_1P1T_NO_CK_KSC6xxJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

