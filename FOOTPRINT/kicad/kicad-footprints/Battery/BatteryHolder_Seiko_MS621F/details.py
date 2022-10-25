
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Battery"
    oIndex = "BatteryHolder_Seiko_MS621F"
    hexID = "FZKBATBATHOLDERSEIKOMS621F"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BatteryHolder_Seiko_MS621F', 'description': 'Seiko MS621F, https://www.sii.co.jp/en/me/files/2014/02/file_EXTENDED_PRDCT_SPEC_75_FILE_11.jpg', 'tags': 'Seiko MS621F', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Battery.3dshapes/BatteryHolder_Seiko_MS621F.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Battery : BatteryHolder_Seiko_MS621F')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

