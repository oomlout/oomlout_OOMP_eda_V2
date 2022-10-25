
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Texas_DSBGA-49_3.33x3.488mm_Layout7x7_P0.4mm"
    hexID = "FZKBGATEXASDSBGA49333X3488LAYOUT7X7P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_DSBGA-49_3.33x3.488mm_Layout7x7_P0.4mm', 'description': 'Texas Instruments, DSBGA, 3.33x3.488x0.625mm, 49 ball 7x7 area grid, NSMD pad definition (http://www.ti.com/lit/ds/symlink/msp430f2234.pdf, http://www.ti.com/lit/an/snva009ag/snva009ag.pdf)', 'tags': 'texas dsbga 49', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_DSBGA-49_3.33x3.488mm_Layout7x7_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Texas_DSBGA-49_3.33x3.488mm_Layout7x7_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

