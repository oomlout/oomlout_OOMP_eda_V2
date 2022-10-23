
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_Push_1P1T-SH_NO_CK_KMR2xxG"
    hexID = "FZKBSWITCHSMSWPUSH1P1TSHNOCKKMR2XXG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_Push_1P1T-SH_NO_CK_KMR2xxG', 'description': 'CK components KMR2 tactile switch with ground pin http://www.ckswitches.com/media/1479/kmr2.pdf', 'tags': 'tactile switch kmr2', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_Push_1P1T-SH_NO_CK_KMR2xxG.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_Push_1P1T-SH_NO_CK_KMR2xxG')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

