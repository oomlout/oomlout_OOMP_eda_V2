
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_THT"
    oIndex = "SW_Push_2P2T_Vertical_E-Switch_800UDP8P1A1M6"
    hexID = "FZKBSWPUSH2P2TVERTICALESWITCH8UDP8P1A1M6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_Push_2P2T_Vertical_E-Switch_800UDP8P1A1M6', 'description': ' right angle DPDT push button https://www.e-switch.com/system/asset/product_line/data_sheet/210/800U.pdf', 'tags': 'IP67 ultra-miniture horizontal', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_Push_2P2T_Vertical_E-Switch_800UDP8P1A1M6.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Button_Switch_THT : SW_Push_2P2T_Vertical_E-Switch_800UDP8P1A1M6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

