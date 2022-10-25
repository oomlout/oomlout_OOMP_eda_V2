
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_THT"
    oIndex = "Push_E-Switch_KS01Q01"
    hexID = "FZKBPUSHESWITCHKS1Q1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Push_E-Switch_KS01Q01', 'description': 'E-Switch KS01Q01 http://spec_sheets.e-switch.com/specs/29-KS01Q01.pdf', 'tags': 'Push Button', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/Push_E-Switch_KS01Q01.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Button_Switch_THT : Push_E-Switch_KS01Q01')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

