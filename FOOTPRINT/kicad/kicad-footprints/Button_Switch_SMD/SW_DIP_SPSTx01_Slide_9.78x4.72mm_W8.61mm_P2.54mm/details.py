
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_DIP_SPSTx01_Slide_9.78x4.72mm_W8.61mm_P2.54mm"
    hexID = "FZKBSWITCHSMSWDIPSPSTX1SLIDE978X472W861P254"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_DIP_SPSTx01_Slide_9.78x4.72mm_W8.61mm_P2.54mm', 'description': 'SMD 1x-dip-switch SPST , Slide, row spacing 8.61 mm (338 mils), body size 9.78x4.72mm (see e.g. https://www.ctscorp.com/wp-content/uploads/204.pdf), SMD', 'tags': 'SMD DIP Switch SPST Slide 8.61mm 338mil SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_DIP_SPSTx01_Slide_9.78x4.72mm_W8.61mm_P2.54mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_DIP_SPSTx01_Slide_9.78x4.72mm_W8.61mm_P2.54mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

