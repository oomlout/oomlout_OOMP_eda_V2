
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_THT"
    oIndex = "SW_Slide_1P2T_CK_OS102011MS2Q"
    hexID = "FZKBSWSLIDE1P2TCKOS1211MS2Q"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_Slide_1P2T_CK_OS102011MS2Q', 'description': 'CuK miniature slide switch, OS series, SPDT, https://www.ckswitches.com/media/1428/os.pdf', 'tags': 'switch SPDT', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_Slide_1P2T_CK_OS102011MS2Q.wrl', 'pins': {'type': 'thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Button_Switch_THT : SW_Slide_1P2T_CK_OS102011MS2Q')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

