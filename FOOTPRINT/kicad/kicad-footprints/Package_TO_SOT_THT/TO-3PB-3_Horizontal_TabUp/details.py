
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "TO-3PB-3_Horizontal_TabUp"
    hexID = "FZKSOTTO3PB3HORIZONTALTABUP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-3PB-3_Horizontal_TabUp', 'description': 'TO-3PB-3, Horizontal, RM 5.45mm, , see http://www.onsemi.com/pub/Collateral/340AC.PDF', 'tags': 'TO-3PB-3 Horizontal RM 5.45mm ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-3PB-3_Horizontal_TabUp.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Package_TO_SOT_THT : TO-3PB-3_Horizontal_TabUp')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

