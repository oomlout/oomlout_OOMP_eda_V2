
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_DIP_SPSTx10_Slide_KingTek_DSHP10TS_W7.62mm_P1.27mm"
    hexID = "FZKBSWITCHSMSWDIPSPSTX1SLIDEKINGTEKDSHP1TSW762P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_DIP_SPSTx10_Slide_KingTek_DSHP10TS_W7.62mm_P1.27mm', 'description': 'SMD 10x-dip-switch SPST KingTek_DSHP10TS, Slide, row spacing 7.62 mm (300 mils), body size  (see http://www.kingtek.net.cn/pic/201601201417455112.pdf)', 'tags': 'SMD DIP Switch SPST Slide 7.62mm 300mil', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_DIP_SPSTx10_Slide_KingTek_DSHP10TS_W7.62mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_DIP_SPSTx10_Slide_KingTek_DSHP10TS_W7.62mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

