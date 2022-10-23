
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_SP3T_PCM13"
    hexID = "FZKBSWITCHSMSWSP3TPCM13"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_SP3T_PCM13', 'description': 'Ultraminiature Surface Mount Slide Switch, right-angle, https://www.ckswitches.com/media/1424/pcm.pdf', 'tags': None, 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_SP3T_PCM13.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_SP3T_PCM13')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

