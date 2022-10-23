
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_THT"
    oIndex = "SW_PUSH-12mm_Wuerth-430476085716"
    hexID = "FZKBSWPUSH12WUERTH4347685716"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_PUSH-12mm_Wuerth-430476085716', 'description': 'SW PUSH 12mm http://katalog.we-online.de/em/datasheet/430476085716.pdf', 'tags': 'tact sw push 12mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_PUSH-12mm_Wuerth-430476085716.wrl', 'pins': {'type': 'thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Button_Switch_THT : SW_PUSH-12mm_Wuerth-430476085716')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

