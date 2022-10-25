
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_RJ"
    oIndex = "RJ45_Wuerth_7499010001A_Horizontal"
    hexID = "FZKCNRJRJ45WUERTH749911AHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RJ45_Wuerth_7499010001A_Horizontal', 'description': '10/100Base-TX RJ45 ethernet magnetic transformer connector horizontal https://katalog.we-online.de/pbs/datasheet/7499010001A.pdf', 'tags': 'RJ45 ethernet magnetic', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_Wuerth_7499010001A_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_RJ : RJ45_Wuerth_7499010001A_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

