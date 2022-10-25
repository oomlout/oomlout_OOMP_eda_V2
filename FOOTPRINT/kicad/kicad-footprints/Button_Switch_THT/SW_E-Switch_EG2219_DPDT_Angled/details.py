
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_THT"
    oIndex = "SW_E-Switch_EG2219_DPDT_Angled"
    hexID = "FZKBSWESWITCHEG2219DPDTANGL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_E-Switch_EG2219_DPDT_Angled', 'description': 'E-Switch slide switch, EG series, DPDT, right angle, http://spec_sheets.e-switch.com/specs/P040170.pdf', 'tags': 'switch DPDT', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_E-Switch_EG2219_DPDT_Angled.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Button_Switch_THT : SW_E-Switch_EG2219_DPDT_Angled')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

