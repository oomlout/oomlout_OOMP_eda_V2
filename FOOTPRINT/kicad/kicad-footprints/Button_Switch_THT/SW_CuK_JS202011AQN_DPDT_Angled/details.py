
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_THT"
    oIndex = "SW_CuK_JS202011AQN_DPDT_Angled"
    hexID = "FZKBSWCUKJS2211AQNDPDTANGL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_CuK_JS202011AQN_DPDT_Angled', 'description': 'CuK sub miniature slide switch, JS series, DPDT, right angle, http://www.ckswitches.com/media/1422/js.pdf', 'tags': 'switch DPDT', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_CuK_JS202011AQN_DPDT_Angled.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_THT : SW_CuK_JS202011AQN_DPDT_Angled')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

