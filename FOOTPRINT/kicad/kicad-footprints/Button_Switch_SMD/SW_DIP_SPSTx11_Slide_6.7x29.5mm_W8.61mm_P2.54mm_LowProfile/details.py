
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_DIP_SPSTx11_Slide_6.7x29.5mm_W8.61mm_P2.54mm_LowProfile"
    hexID = "FZKBSWITCHSMSWDIPSPSTX11SLIDE67X295W861P254LOWPROFILE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_DIP_SPSTx11_Slide_6.7x29.5mm_W8.61mm_P2.54mm_LowProfile', 'description': 'SMD 11x-dip-switch SPST , Slide, row spacing 8.61 mm (338 mils), body size 6.7x29.5mm (see e.g. https://www.ctscorp.com/wp-content/uploads/219.pdf), SMD, LowProfile', 'tags': 'SMD DIP Switch SPST Slide 8.61mm 338mil SMD LowProfile', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_DIP_SPSTx11_Slide_6.7x29.5mm_W8.61mm_P2.54mm_LowProfile.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_DIP_SPSTx11_Slide_6.7x29.5mm_W8.61mm_P2.54mm_LowProfile')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

