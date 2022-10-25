
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_Osram_Lx_P47F_D2mm_ReverseMount"
    hexID = "FZKLSMLOSRAMLXP47FD2RMOUNT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_Osram_Lx_P47F_D2mm_ReverseMount', 'description': 'OSRAM, reverse-mount LED, SMD, 2mm diameter, http://www.farnell.com/datasheets/2711587.pdf', 'tags': 'LED ReverseMount Reverse', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Osram_Lx_P47F_D2mm_ReverseMount.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('LED_SMD : LED_Osram_Lx_P47F_D2mm_ReverseMount')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

