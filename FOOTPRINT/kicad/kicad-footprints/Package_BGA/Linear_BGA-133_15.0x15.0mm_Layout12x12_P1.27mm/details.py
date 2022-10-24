
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Linear_BGA-133_15.0x15.0mm_Layout12x12_P1.27mm"
    hexID = "FZKBGALINEARBGA13315X15LAYOUT12X12P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Linear_BGA-133_15.0x15.0mm_Layout12x12_P1.27mm', 'description': 'Analog Devices (Linear Tech), 133-pin BGA uModule, 15.0x15.0x4.92mm, https://www.analog.com/media/en/technical-documentation/data-sheets/4637fc.pdf', 'tags': '133 pin bga', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Linear_BGA-133_15.0x15.0mm_Layout12x12_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Linear_BGA-133_15.0x15.0mm_Layout12x12_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

