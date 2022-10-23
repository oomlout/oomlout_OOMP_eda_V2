
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_DIP_SPSTx09_Slide_Omron_A6S-910x_W8.9mm_P2.54mm"
    hexID = "FZKBSWITCHSMSWDIPSPSTX9SLIDEOMRONA6S91XW89P254"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_DIP_SPSTx09_Slide_Omron_A6S-910x_W8.9mm_P2.54mm', 'description': 'SMD 9x-dip-switch SPST Omron_A6S-910x, Slide, row spacing 8.9 mm (350 mils), body size  (see http://omronfs.omron.com/en_US/ecb/products/pdf/en-a6s.pdf)', 'tags': 'SMD DIP Switch SPST Slide 8.9mm 350mil', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_DIP_SPSTx09_Slide_Omron_A6S-910x_W8.9mm_P2.54mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_DIP_SPSTx09_Slide_Omron_A6S-910x_W8.9mm_P2.54mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

