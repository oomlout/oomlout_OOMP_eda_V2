
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Texas_DSBGA-28_1.9x3.0mm_Layout4x7_P0.4mm"
    hexID = "FZKBGATEXASDSBGA2819X3LAYOUT4X7P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_DSBGA-28_1.9x3.0mm_Layout4x7_P0.4mm', 'description': 'Texas Instruments, DSBGA, 3.0x1.9x0.625mm, 28 ball 7x4 area grid, NSMD pad definition (http://www.ti.com/lit/ds/symlink/bq51050b.pdf, http://www.ti.com/lit/an/snva009ag/snva009ag.pdf)', 'tags': 'BGA 28 0.4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_DSBGA-28_1.9x3.0mm_Layout4x7_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Texas_DSBGA-28_1.9x3.0mm_Layout4x7_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

