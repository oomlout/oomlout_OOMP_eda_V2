
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "BGA-9_1.6x1.6mm_Layout3x3_P0.5mm"
    hexID = "FZKBGABGA916X16LAYOUT3X3P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BGA-9_1.6x1.6mm_Layout3x3_P0.5mm', 'description': 'BGA-9, http://www.ti.com/lit/ds/symlink/bq27421-g1.pdf', 'tags': 'BGA-9', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-9_1.6x1.6mm_Layout3x3_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : BGA-9_1.6x1.6mm_Layout3x3_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

