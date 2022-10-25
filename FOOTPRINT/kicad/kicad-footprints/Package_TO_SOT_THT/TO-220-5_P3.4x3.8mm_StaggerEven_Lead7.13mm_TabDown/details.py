
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "TO-220-5_P3.4x3.8mm_StaggerEven_Lead7.13mm_TabDown"
    hexID = "FZKSOTTO225P34X38STAGGEREVENLEAD713TABDOWN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-220-5_P3.4x3.8mm_StaggerEven_Lead7.13mm_TabDown', 'description': 'TO-220-5, Horizontal, RM 1.7mm, Pentawatt, Multiwatt-5, staggered type-2, see http://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/ltc-legacy-to-220/to-220_5_05-08-1421.pdf?domain=www.linear.com, https://www.diodes.com/assets/Package-Files/TO220-5.pdf', 'tags': 'TO-220-5 Horizontal RM 1.7mm Pentawatt Multiwatt-5 staggered type-2', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-220-5_P3.4x3.8mm_StaggerEven_Lead7.13mm_TabDown.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Package_TO_SOT_THT : TO-220-5_P3.4x3.8mm_StaggerEven_Lead7.13mm_TabDown')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

