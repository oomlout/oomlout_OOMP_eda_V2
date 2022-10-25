
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_IDT_JU6-6_7.0x5.0mm_P2.54mm"
    hexID = "FZKOCSOCSSMIDTJU667X5P254"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_IDT_JU6-6_7.0x5.0mm_P2.54mm', 'description': 'SMD Crystal Oscillator IDT https://www.idt.com/document/dst/xu-family-datasheet#page=17, 7.0x5.0mm', 'tags': 'SMD SMT crystal oscillator', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_IDT_JU6-6_7.0x5.0mm_P2.54mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_IDT_JU6-6_7.0x5.0mm_P2.54mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

