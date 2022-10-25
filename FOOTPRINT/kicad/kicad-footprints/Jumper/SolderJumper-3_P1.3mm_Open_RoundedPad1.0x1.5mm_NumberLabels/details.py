
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Jumper"
    oIndex = "SolderJumper-3_P1.3mm_Open_RoundedPad1.0x1.5mm_NumberLabels"
    hexID = "FZKJSOLDERJ3P13OPENROUNDEDPAD1X15NUMBERLABELS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SolderJumper-3_P1.3mm_Open_RoundedPad1.0x1.5mm_NumberLabels', 'description': 'SMD Solder 3-pad Jumper, 1x1.5mm rounded Pads, 0.3mm gap, open, labeled with numbers', 'tags': 'solder jumper open', 'attributeType': None, 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Jumper : SolderJumper-3_P1.3mm_Open_RoundedPad1.0x1.5mm_NumberLabels')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

