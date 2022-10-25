
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_DIP_SPSTx07_Slide_6.7x19.34mm_W6.73mm_P2.54mm_LowProfile_JPin"
    hexID = "FZKBSWITCHSMSWDIPSPSTX7SLIDE67X1934W673P254LOWPROFILEJPIN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_DIP_SPSTx07_Slide_6.7x19.34mm_W6.73mm_P2.54mm_LowProfile_JPin', 'description': 'SMD 7x-dip-switch SPST , Slide, row spacing 6.73 mm (264 mils), body size 6.7x19.34mm (see e.g. https://www.ctscorp.com/wp-content/uploads/219.pdf), SMD, LowProfile, JPin', 'tags': 'SMD DIP Switch SPST Slide 6.73mm 264mil SMD LowProfile JPin', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_DIP_SPSTx07_Slide_6.7x19.34mm_W6.73mm_P2.54mm_LowProfile_JPin.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_DIP_SPSTx07_Slide_6.7x19.34mm_W6.73mm_P2.54mm_LowProfile_JPin')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

