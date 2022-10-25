
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_DPDT_CK_JS202011JCQN"
    hexID = "FZKBSWITCHSMSWDPDTCKJS2211JCQN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_DPDT_CK_JS202011JCQN', 'description': 'Sub-miniature slide switch, vertical, SMT J bend https://dznh3ojzb2azq.cloudfront.net/products/Slide/JS/documents/datasheet.pdf', 'tags': 'switch DPDT SMT', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_DPDT_CK_JS202011JCQN.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_DPDT_CK_JS202011JCQN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

