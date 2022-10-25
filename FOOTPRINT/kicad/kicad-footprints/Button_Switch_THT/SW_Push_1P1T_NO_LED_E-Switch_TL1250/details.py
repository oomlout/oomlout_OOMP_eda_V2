
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_THT"
    oIndex = "SW_Push_1P1T_NO_LED_E-Switch_TL1250"
    hexID = "FZKBSWPUSH1P1TNOLESWITCHTL125"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_Push_1P1T_NO_LED_E-Switch_TL1250', 'description': 'illuminated right angle tact switch https://www.e-switch.com/system/asset/product_line/data_sheet/148/TL1250.pdf', 'tags': 'led push switch right angle', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_Push_1P1T_NO_LED_E-Switch_TL1250.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Button_Switch_THT : SW_Push_1P1T_NO_LED_E-Switch_TL1250')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

