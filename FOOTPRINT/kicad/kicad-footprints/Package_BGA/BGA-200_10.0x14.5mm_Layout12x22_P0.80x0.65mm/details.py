
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "BGA-200_10.0x14.5mm_Layout12x22_P0.80x0.65mm"
    hexID = "FZKBGABGA21X145LAYOUT12X22P8X65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BGA-200_10.0x14.5mm_Layout12x22_P0.80x0.65mm', 'description': 'BGA-200, 14.5x10.0mm, 200 Ball, 12x22 Layout, 0.8x0.65mm Pitch, http://www.issi.com/WW/pdf/43-46LQ32256A-AL.pdf', 'tags': 'BGA 200 0.8x0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-200_10.0x14.5mm_Layout12x22_P0.80x0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : BGA-200_10.0x14.5mm_Layout12x22_P0.80x0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

