
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_Push_1P1T_NO_Vertical_Wuerth_434133025816"
    hexID = "FZKBSWITCHSMSWPUSH1P1TNOVERTICALWUERTH43413325816"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_Push_1P1T_NO_Vertical_Wuerth_434133025816', 'description': 'https://katalog.we-online.com/em/datasheet/434133025816.pdf', 'tags': 'tactile switch Wurth Wuerth', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_Push_1P1T_NO_Vertical_Wuerth_434133025816.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_Push_1P1T_NO_Vertical_Wuerth_434133025816')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

