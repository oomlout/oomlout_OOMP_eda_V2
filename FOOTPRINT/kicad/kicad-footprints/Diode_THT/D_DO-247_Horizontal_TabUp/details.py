
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "D_DO-247_Horizontal_TabUp"
    hexID = "FZKDDDO247HORIZONTALTABUP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_DO-247_Horizontal_TabUp', 'description': 'Diode, DO-247 series, Horizontal, TabUp, P 10.9mm', 'tags': 'diode rectifier', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_DO-247_Horizontal_TabUp.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Diode_THT : D_DO-247_Horizontal_TabUp')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

