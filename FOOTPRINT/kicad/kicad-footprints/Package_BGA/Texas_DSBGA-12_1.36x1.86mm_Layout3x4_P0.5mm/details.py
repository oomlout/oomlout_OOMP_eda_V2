
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Texas_DSBGA-12_1.36x1.86mm_Layout3x4_P0.5mm"
    hexID = "FZKBGATEXASDSBGA12136X186LAYOUT3X4P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_DSBGA-12_1.36x1.86mm_Layout3x4_P0.5mm', 'description': 'Texas Instruments, DSBGA, 1.36x1.86mm, 12 bump 3x4 (area) array, NSMD pad definition (http://www.ti.com/lit/ds/symlink/txs0104e.pdf, http://www.ti.com/lit/an/snva009ag/snva009ag.pdf)', 'tags': 'Texas Instruments DSBGA BGA', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_DSBGA-12_1.36x1.86mm_Layout3x4_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_BGA : Texas_DSBGA-12_1.36x1.86mm_Layout3x4_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

