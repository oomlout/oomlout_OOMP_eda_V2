
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_Push_SPST_NO_Alps_SKRK"
    hexID = "FZKBSWITCHSMSWPUSHSPSTNOALPSSKRK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_Push_SPST_NO_Alps_SKRK', 'description': 'http://www.alps.com/prod/info/E/HTML/Tact/SurfaceMount/SKRK/SKRKAHE020.html', 'tags': 'SMD SMT button', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_Push_SPST_NO_Alps_SKRK.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Button_Switch_SMD : SW_Push_SPST_NO_Alps_SKRK')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

