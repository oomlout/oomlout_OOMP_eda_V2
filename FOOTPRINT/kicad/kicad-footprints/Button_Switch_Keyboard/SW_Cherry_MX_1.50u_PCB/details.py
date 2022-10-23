
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_Keyboard"
    oIndex = "SW_Cherry_MX_1.50u_PCB"
    hexID = "FZKBSWCHERRYMX15UPCB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_Cherry_MX_1.50u_PCB', 'description': 'Cherry MX keyswitch, 1.50u, PCB mount, http://cherryamericas.com/wp-content/uploads/2014/12/mx_cat.pdf', 'tags': 'Cherry MX keyswitch 1.50u PCB', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_Keyboard.3dshapes/SW_Cherry_MX_1.50u_PCB.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Button_Switch_Keyboard : SW_Cherry_MX_1.50u_PCB')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

