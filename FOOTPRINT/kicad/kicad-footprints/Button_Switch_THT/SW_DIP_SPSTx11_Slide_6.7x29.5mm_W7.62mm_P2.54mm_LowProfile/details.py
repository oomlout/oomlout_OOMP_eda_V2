
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_THT"
    oIndex = "SW_DIP_SPSTx11_Slide_6.7x29.5mm_W7.62mm_P2.54mm_LowProfile"
    hexID = "FZKBSWDIPSPSTX11SLIDE67X295W762P254LOWPROFILE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_DIP_SPSTx11_Slide_6.7x29.5mm_W7.62mm_P2.54mm_LowProfile', 'description': '11x-dip-switch SPST , Slide, row spacing 7.62 mm (300 mils), body size 6.7x29.5mm (see e.g. https://www.ctscorp.com/wp-content/uploads/209-210.pdf), LowProfile', 'tags': 'DIP Switch SPST Slide 7.62mm 300mil LowProfile', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_DIP_SPSTx11_Slide_6.7x29.5mm_W7.62mm_P2.54mm_LowProfile.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_THT : SW_DIP_SPSTx11_Slide_6.7x29.5mm_W7.62mm_P2.54mm_LowProfile')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

