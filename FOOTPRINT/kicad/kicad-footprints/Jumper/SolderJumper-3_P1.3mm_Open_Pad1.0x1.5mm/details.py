
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Jumper"
    oIndex = "SolderJumper-3_P1.3mm_Open_Pad1.0x1.5mm"
    hexID = "FZKJSOLDERJ3P13OPENPAD1X15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SolderJumper-3_P1.3mm_Open_Pad1.0x1.5mm', 'description': 'SMD Solder 3-pad Jumper, 1x1.5mm Pads, 0.3mm gap, open', 'tags': 'solder jumper open', 'attributeType': None, 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Jumper : SolderJumper-3_P1.3mm_Open_Pad1.0x1.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

