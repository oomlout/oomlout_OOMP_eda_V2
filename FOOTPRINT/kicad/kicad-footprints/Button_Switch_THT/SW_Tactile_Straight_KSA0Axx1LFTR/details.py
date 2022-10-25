
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_THT"
    oIndex = "SW_Tactile_Straight_KSA0Axx1LFTR"
    hexID = "FZKBSWTACTILESKSAAXX1LFTR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_Tactile_Straight_KSA0Axx1LFTR', 'description': 'SW PUSH SMALL http://www.ckswitches.com/media/1457/ksa_ksl.pdf', 'tags': 'SW PUSH SMALL Tactile C&K', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_Tactile_Straight_KSA0Axx1LFTR.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Button_Switch_THT : SW_Tactile_Straight_KSA0Axx1LFTR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

