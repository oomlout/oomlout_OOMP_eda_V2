
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_DIP_SPSTx01_Slide_Copal_CHS-01A_W5.08mm_P1.27mm_JPin"
    hexID = "FZKBSWITCHSMSWDIPSPSTX1SLIDECOPALCHS1AW58P127JPIN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_DIP_SPSTx01_Slide_Copal_CHS-01A_W5.08mm_P1.27mm_JPin', 'description': 'SMD 1x-dip-switch SPST Copal_CHS-01A, Slide, row spacing 5.08 mm (200 mils), body size  (see http://www.nidec-copal-electronics.com/e/catalog/switch/chs.pdf), SMD, JPin', 'tags': 'SMD DIP Switch SPST Slide 5.08mm 200mil SMD JPin', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_DIP_SPSTx01_Slide_Copal_CHS-01A_W5.08mm_P1.27mm_JPin.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_DIP_SPSTx01_Slide_Copal_CHS-01A_W5.08mm_P1.27mm_JPin')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

