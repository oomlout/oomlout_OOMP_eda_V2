
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_DIP_SPSTx01_Slide_Copal_CVS-01xB_W5.9mm_P1mm"
    hexID = "FZKBSWITCHSMSWDIPSPSTX1SLIDECOPALCVS1XBW59P1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_DIP_SPSTx01_Slide_Copal_CVS-01xB_W5.9mm_P1mm', 'description': 'SMD 1x-dip-switch SPST Copal_CVS-01xB, Slide, row spacing 5.9 mm (232 mils), body size  (see http://www.nidec-copal-electronics.com/e/catalog/switch/cvs.pdf)', 'tags': 'SMD DIP Switch SPST Slide 5.9mm 232mil', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_DIP_SPSTx01_Slide_Copal_CVS-01xB_W5.9mm_P1mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_DIP_SPSTx01_Slide_Copal_CVS-01xB_W5.9mm_P1mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

