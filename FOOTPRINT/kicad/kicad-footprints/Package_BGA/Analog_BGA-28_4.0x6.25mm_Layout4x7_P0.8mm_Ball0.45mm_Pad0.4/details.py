
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Analog_BGA-28_4.0x6.25mm_Layout4x7_P0.8mm_Ball0.45mm_Pad0.4"
    hexID = "FZKBGAANALOGBGA284X625LAYOUT4X7P8BALL45PAD4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Analog_BGA-28_4.0x6.25mm_Layout4x7_P0.8mm_Ball0.45mm_Pad0.4', 'description': 'Analog BGA-28 4.0mm x 6.25mm package, pitch 0.4mm pad, based on https://www.analog.com/media/en/technical-documentation/data-sheets/8063fa.pdf', 'tags': 'BGA 28 0.8', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Analog_BGA-28_4.0x6.25mm_Layout4x7_P0.8mm_Ball0.45mm_Pad0.4.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Analog_BGA-28_4.0x6.25mm_Layout4x7_P0.8mm_Ball0.45mm_Pad0.4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

