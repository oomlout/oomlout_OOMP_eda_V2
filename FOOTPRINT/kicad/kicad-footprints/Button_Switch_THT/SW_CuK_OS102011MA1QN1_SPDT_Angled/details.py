
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_THT"
    oIndex = "SW_CuK_OS102011MA1QN1_SPDT_Angled"
    hexID = "FZKBSWCUKOS1211MA1QN1SPDTANGL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_CuK_OS102011MA1QN1_SPDT_Angled', 'description': 'CuK miniature slide switch, OS series, SPDT, right angle, http://www.ckswitches.com/media/1428/os.pdf', 'tags': 'switch SPDT', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_CuK_OS102011MA1QN1_SPDT_Angled.wrl', 'pins': {'type': 'thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Button_Switch_THT : SW_CuK_OS102011MA1QN1_SPDT_Angled')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

