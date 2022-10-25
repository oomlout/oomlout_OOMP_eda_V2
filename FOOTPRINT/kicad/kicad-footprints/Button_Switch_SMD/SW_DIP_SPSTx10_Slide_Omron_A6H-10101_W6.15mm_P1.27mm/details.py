
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_DIP_SPSTx10_Slide_Omron_A6H-10101_W6.15mm_P1.27mm"
    hexID = "FZKBSWITCHSMSWDIPSPSTX1SLIDEOMRONA6H111W615P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_DIP_SPSTx10_Slide_Omron_A6H-10101_W6.15mm_P1.27mm', 'description': 'SMD 10x-dip-switch SPST Omron_A6H-10101, Slide, row spacing 6.15 mm (242 mils), body size  (see https://www.omron.com/ecb/products/pdf/en-a6h.pdf)', 'tags': 'SMD DIP Switch SPST Slide 6.15mm 242mil', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_DIP_SPSTx10_Slide_Omron_A6H-10101_W6.15mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_DIP_SPSTx10_Slide_Omron_A6H-10101_W6.15mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

