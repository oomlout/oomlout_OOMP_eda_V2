
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "TO-264-3_Horizontal_TabDown"
    hexID = "FZKSOTTO2643HORIZONTALTABDOWN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-264-3_Horizontal_TabDown', 'description': 'TO-264-3, Horizontal, RM 5.45mm, see https://www.fairchildsemi.com/package-drawings/TO/TO264A03.pdf', 'tags': 'TO-264-3 Horizontal RM 5.45mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-264-3_Horizontal_TabDown.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Package_TO_SOT_THT : TO-264-3_Horizontal_TabDown')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

