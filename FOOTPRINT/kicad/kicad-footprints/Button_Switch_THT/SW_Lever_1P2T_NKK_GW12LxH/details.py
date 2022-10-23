
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_THT"
    oIndex = "SW_Lever_1P2T_NKK_GW12LxH"
    hexID = "FZKBSWLEVER1P2TNKKGW12LXH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_Lever_1P2T_NKK_GW12LxH', 'description': 'Switch, single pole double throw, right angle, http://www.nkkswitches.com/pdf/GW.pdf', 'tags': 'switch single-pole double-throw spdt ON-ON horizontal', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_Lever_1P2T_NKK_GW12LxH.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Button_Switch_THT : SW_Lever_1P2T_NKK_GW12LxH')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

