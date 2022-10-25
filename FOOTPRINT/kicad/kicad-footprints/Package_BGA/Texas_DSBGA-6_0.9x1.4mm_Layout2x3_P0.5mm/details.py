
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Texas_DSBGA-6_0.9x1.4mm_Layout2x3_P0.5mm"
    hexID = "FZKBGATEXASDSBGA69X14LAYOUT2X3P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_DSBGA-6_0.9x1.4mm_Layout2x3_P0.5mm', 'description': 'Texas Instruments, DSBGA, 0.9x1.4mm, 6 bump 2x3 (perimeter) array, NSMD pad definition (http://www.ti.com/lit/ds/symlink/ts5a3159a.pdf)', 'tags': 'Texas Instruments DSBGA BGA YZP R-XBGA-N6', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_DSBGA-6_0.9x1.4mm_Layout2x3_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_BGA : Texas_DSBGA-6_0.9x1.4mm_Layout2x3_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

