
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_Push_1P1T_NO_CK_KSC7xxJ"
    hexID = "FZKBSWITCHSMSWPUSH1P1TNOCKKSC7XXJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_Push_1P1T_NO_CK_KSC7xxJ', 'description': 'CK components KSC7 tactile switch https://www.ckswitches.com/media/1973/ksc7.pdf', 'tags': 'tactile switch ksc7', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_push_1P1T_NO_CK_KSC7xxJxxx.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_Push_1P1T_NO_CK_KSC7xxJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

