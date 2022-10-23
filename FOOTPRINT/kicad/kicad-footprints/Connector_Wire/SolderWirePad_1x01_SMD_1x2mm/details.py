
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Wire"
    oIndex = "SolderWirePad_1x01_SMD_1x2mm"
    hexID = "FZKCNWIRESOLDERWIREPAD1X1SM1X2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SolderWirePad_1x01_SMD_1x2mm', 'description': 'Wire Pad, Square, SMD Pad,  5mm x 10mm,', 'tags': 'MesurementPoint Square SMDPad 5mmx10mm ', 'attributeType': None, 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Wire : SolderWirePad_1x01_SMD_1x2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

