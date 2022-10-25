
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_THT"
    oIndex = "SW_PUSH_E-Switch_FS5700DP_DPDT"
    hexID = "FZKBSWPUSHESWITCHFS57DPDPDT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_PUSH_E-Switch_FS5700DP_DPDT', 'description': 'FS5700 series pushbutton footswitch, DPDT, https://www.e-switch.com/system/asset/product_line/data_sheet/226/FS5700.pdf', 'tags': 'switch DPDT footswitch', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_PUSH_E-Switch_FS5700DP_DPDT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_THT : SW_PUSH_E-Switch_FS5700DP_DPDT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

