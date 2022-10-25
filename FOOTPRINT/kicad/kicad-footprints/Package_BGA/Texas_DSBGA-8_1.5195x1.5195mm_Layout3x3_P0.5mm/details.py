
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Texas_DSBGA-8_1.5195x1.5195mm_Layout3x3_P0.5mm"
    hexID = "FZKBGATEXASDSBGA815195X15195LAYOUT3X3P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_DSBGA-8_1.5195x1.5195mm_Layout3x3_P0.5mm', 'description': 'Texas Instruments, DSBGA, 1.5195x1.5195x0.600mm, 8 ball 3x3 area grid, YZR pad definition (http://www.ti.com/lit/ml/mxbg270/mxbg270.pdf)', 'tags': 'BGA 8 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_DSBGA-8_1.5195x1.5195mm_Layout3x3_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Texas_DSBGA-8_1.5195x1.5195mm_Layout3x3_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

