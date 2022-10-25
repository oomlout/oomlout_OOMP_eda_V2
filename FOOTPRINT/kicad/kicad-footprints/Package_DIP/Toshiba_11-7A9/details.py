
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "Toshiba_11-7A9"
    hexID = "FZKDIPTOSHIBA117A9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Toshiba_11-7A9', 'description': 'Toshiba 11-7A9 package, like 6-lead dip package with missing pin 5, row spacing 7.62 mm (300 mils), https://toshiba.semicon-storage.com/info/docget.jsp?did=1421&prodName=TLP3021(S)', 'tags': 'Toshiba 11-7A9 DIL DIP PDIP 2.54mm 7.62mm 300mil', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/Toshiba_11-7A9.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : Toshiba_11-7A9')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

