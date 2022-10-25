
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "BatteryHolder_Keystone_1057_1x2032"
    hexID = "FZKBATBATHOLDERKEYSTONE1571X232"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BatteryHolder_Keystone_1057_1x2032', 'description': 'SMT (Auto-In/Ultra-Low) Holder for 2032 Cell, 33.2 x 23.9mm, 2mm height above PCB, https://www.keyelco.com/userAssets/file/M65p4.pdf', 'tags': 'Keystone type 1057 coin cell holder', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_Keystone_1057_1x2032.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Battery : BatteryHolder_Keystone_1057_1x2032')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

