
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_THT"
    oIndex = "SW_DIP_SPSTx02_Slide_9.78x7.26mm_W7.62mm_P2.54mm"
    hexID = "FZKBSWDIPSPSTX2SLIDE978X726W762P254"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_DIP_SPSTx02_Slide_9.78x7.26mm_W7.62mm_P2.54mm', 'description': '2x-dip-switch SPST , Slide, row spacing 7.62 mm (300 mils), body size 9.78x7.26mm (see e.g. https://www.ctscorp.com/wp-content/uploads/206-208.pdf)', 'tags': 'DIP Switch SPST Slide 7.62mm 300mil', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_DIP_SPSTx02_Slide_9.78x7.26mm_W7.62mm_P2.54mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_THT : SW_DIP_SPSTx02_Slide_9.78x7.26mm_W7.62mm_P2.54mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

