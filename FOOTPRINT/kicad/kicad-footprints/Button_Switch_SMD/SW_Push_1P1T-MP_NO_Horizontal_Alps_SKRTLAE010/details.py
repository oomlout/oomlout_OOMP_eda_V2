
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_Push_1P1T-MP_NO_Horizontal_Alps_SKRTLAE010"
    hexID = "FZKBSWITCHSMSWPUSH1P1TMPNOHORIZONTALALPSSKRTLAE1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_Push_1P1T-MP_NO_Horizontal_Alps_SKRTLAE010', 'description': 'Side push button (https://www.alps.com/prod/info/E/PDF/Tact/SurfaceMount/SKRT/SKRT.pdf)', 'tags': 'push horizontal SPST 1P1T', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_Push_1P1T-MP_NO_Horizontal_Alps_SKRTLAE010.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Button_Switch_SMD : SW_Push_1P1T-MP_NO_Horizontal_Alps_SKRTLAE010')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

