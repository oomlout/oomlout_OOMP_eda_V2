
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_RJ"
    oIndex = "RJ45_Wuerth_74980111211_Horizontal"
    hexID = "FZKCNRJRJ45WUERTH7498111211HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RJ45_Wuerth_74980111211_Horizontal', 'description': 'RJ45 LAN Transformer 10/100BaseT (https://katalog.we-online.de/pbs/datasheet/74980111211.pdf)', 'tags': 'lan magnetics transformer', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_Wuerth_74980111211_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_RJ : RJ45_Wuerth_74980111211_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

