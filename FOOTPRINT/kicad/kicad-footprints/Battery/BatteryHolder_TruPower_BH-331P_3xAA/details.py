
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "BatteryHolder_TruPower_BH-331P_3xAA"
    hexID = "FZKBATBATHOLDERTRUPOWERBH331P3XAA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BatteryHolder_TruPower_BH-331P_3xAA', 'description': 'Keystone Battery Holder BH-331P Battery Type 3xAA (Script generated with StandardBox.py) (Keystone Battery Holder BH-331P Battery Type 3xAA)', 'tags': 'Battery Holder BH-331P Battery Type 3xAA', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_TruPower_BH-331P_3xAA.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Battery : BatteryHolder_TruPower_BH-331P_3xAA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

