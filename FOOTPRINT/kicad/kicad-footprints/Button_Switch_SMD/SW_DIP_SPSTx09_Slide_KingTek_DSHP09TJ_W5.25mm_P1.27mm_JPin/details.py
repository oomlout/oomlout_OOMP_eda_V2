
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_DIP_SPSTx09_Slide_KingTek_DSHP09TJ_W5.25mm_P1.27mm_JPin"
    hexID = "FZKBSWITCHSMSWDIPSPSTX9SLIDEKINGTEKDSHP9TJW525P127JPIN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_DIP_SPSTx09_Slide_KingTek_DSHP09TJ_W5.25mm_P1.27mm_JPin', 'description': 'SMD 9x-dip-switch SPST KingTek_DSHP09TJ, Slide, row spacing 5.25 mm (206 mils), body size  (see http://www.kingtek.net.cn/pic/201601201446313350.pdf), JPin', 'tags': 'SMD DIP Switch SPST Slide 5.25mm 206mil JPin', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_DIP_SPSTx09_Slide_KingTek_DSHP09TJ_W5.25mm_P1.27mm_JPin.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_DIP_SPSTx09_Slide_KingTek_DSHP09TJ_W5.25mm_P1.27mm_JPin')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

