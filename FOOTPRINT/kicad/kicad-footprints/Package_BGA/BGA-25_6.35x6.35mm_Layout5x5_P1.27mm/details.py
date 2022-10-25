
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "BGA-25_6.35x6.35mm_Layout5x5_P1.27mm"
    hexID = "FZKBGABGA25635X635LAYOUT5X5P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BGA-25_6.35x6.35mm_Layout5x5_P1.27mm', 'description': 'BGA-25, http://cds.linear.com/docs/en/datasheet/4624fc.pdf', 'tags': 'BGA-25 uModule', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-25_6.35x6.35mm_Layout5x5_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : BGA-25_6.35x6.35mm_Layout5x5_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

