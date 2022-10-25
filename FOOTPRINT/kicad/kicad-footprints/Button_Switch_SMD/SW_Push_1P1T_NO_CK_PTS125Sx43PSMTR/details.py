
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_Push_1P1T_NO_CK_PTS125Sx43PSMTR"
    hexID = "FZKBSWITCHSMSWPUSH1P1TNOCKPTS125SX43PSMTR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_Push_1P1T_NO_CK_PTS125Sx43PSMTR', 'description': 'C&K Switches 1P1T SMD PTS125 Series 12mm Tact Switch with Pegs, https://www.ckswitches.com/media/1462/pts125.pdf', 'tags': 'Button Tactile Switch SPST 1P1T', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_Push_1P1T_NO_CK_PTS125Sx43PSMTR.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Button_Switch_SMD : SW_Push_1P1T_NO_CK_PTS125Sx43PSMTR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

