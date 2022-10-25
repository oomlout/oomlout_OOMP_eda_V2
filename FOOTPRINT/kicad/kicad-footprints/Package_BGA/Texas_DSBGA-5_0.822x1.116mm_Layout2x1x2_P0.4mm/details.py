
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Texas_DSBGA-5_0.822x1.116mm_Layout2x1x2_P0.4mm"
    hexID = "FZKBGATEXASDSBGA5822X1116LAYOUT2X1X2P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_DSBGA-5_0.822x1.116mm_Layout2x1x2_P0.4mm', 'description': 'Texas Instruments, DSBGA, 0.822x1.116mm, 5 bump 2x1x2 array, NSMD pad definition (http://www.ti.com/lit/ds/symlink/opa330.pdf, http://www.ti.com/lit/an/snva009ag/snva009ag.pdf)', 'tags': 'Texas Instruments DSBGA BGA YFF S-XBGA-N5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_DSBGA-5_0.822x1.116mm_Layout2x1x2_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_BGA : Texas_DSBGA-5_0.822x1.116mm_Layout2x1x2_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

