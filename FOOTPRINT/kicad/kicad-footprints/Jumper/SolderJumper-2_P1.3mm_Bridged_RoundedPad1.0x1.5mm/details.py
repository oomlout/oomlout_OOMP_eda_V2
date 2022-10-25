
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Jumper"
    oIndex = "SolderJumper-2_P1.3mm_Bridged_RoundedPad1.0x1.5mm"
    hexID = "FZKJSOLDERJ2P13BRIDGEDROUNDEDPAD1X15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SolderJumper-2_P1.3mm_Bridged_RoundedPad1.0x1.5mm', 'description': 'SMD Solder Jumper, 1x1.5mm, rounded Pads, 0.3mm gap, bridged with 1 copper strip', 'tags': 'net tie solder jumper bridged', 'attributeType': None, 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Jumper : SolderJumper-2_P1.3mm_Bridged_RoundedPad1.0x1.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

