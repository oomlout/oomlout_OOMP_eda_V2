
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "WLCSP-16_4x4_B2.17x2.32mm_P0.5mm"
    hexID = "FZKCSPWLCSP164X4B217X232P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WLCSP-16_4x4_B2.17x2.32mm_P0.5mm', 'description': 'WLCSP-16, http://www.nxp.com/documents/data_sheet/LPC1102_1104.pdf, http://www.nxp.com/assets/documents/data/en/application-notes/AN3846.pdf', 'tags': 'WLCSP-16 NXP', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/WLCSP-16_4x4_B2.17x2.32mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_CSP : WLCSP-16_4x4_B2.17x2.32mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

