
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "BatteryHolder_Keystone_3002_1x2032"
    hexID = "FZKBATBATHOLDERKEYSTONE321X232"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BatteryHolder_Keystone_3002_1x2032', 'description': 'https://www.tme.eu/it/Document/a823211ec201a9e209042d155fe22d2b/KEYS2996.pdf', 'tags': 'BR2016 CR2016 DL2016 BR2020 CL2020 BR2025 CR2025 DL2025 DR2032 CR2032 DL2032', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_Keystone_3002_1x2032.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Battery : BatteryHolder_Keystone_3002_1x2032')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

