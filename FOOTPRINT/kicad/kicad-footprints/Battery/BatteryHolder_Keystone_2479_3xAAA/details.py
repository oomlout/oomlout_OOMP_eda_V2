
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "BatteryHolder_Keystone_2479_3xAAA"
    hexID = "FZKBATBATHOLDERKEYSTONE24793XAAA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BatteryHolder_Keystone_2479_3xAAA', 'description': 'Keystone Battery Holder, 2479, Battery Type 3xAAA (Script generated with StandardBox.py) (Keystone Battery Holder, 2479, Battery Type 3xAAA)', 'tags': 'Keystone Battery Holder 2479 Battery Type 3xAAA', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_Keystone_2479_3xAAA.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Battery : BatteryHolder_Keystone_2479_3xAAA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

