
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_DIP_SPSTx08_Slide_Copal_CHS-08B_W7.62mm_P1.27mm"
    hexID = "FZKBSWITCHSMSWDIPSPSTX8SLIDECOPALCHS8BW762P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_DIP_SPSTx08_Slide_Copal_CHS-08B_W7.62mm_P1.27mm', 'description': 'SMD 8x-dip-switch SPST Copal_CHS-08B, Slide, row spacing 7.62 mm (300 mils), body size  (see http://www.nidec-copal-electronics.com/e/catalog/switch/chs.pdf), SMD', 'tags': 'SMD DIP Switch SPST Slide 7.62mm 300mil SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_DIP_SPSTx08_Slide_Copal_CHS-08B_W7.62mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_DIP_SPSTx08_Slide_Copal_CHS-08B_W7.62mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

