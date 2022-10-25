
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_RJ"
    oIndex = "RJ45_Cetus_J1B1211CCD_Horizontal"
    hexID = "FZKCNRJRJ45CETUSJ1B1211CCDHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RJ45_Cetus_J1B1211CCD_Horizontal', 'description': '1 Port RJ45 Magjack Connector Through Hole 10/100 Base-T, Cetus, used and distributed by WIZnet (https://wizwiki.net/wiki/lib/exe/fetch.php?media=products:wiz550web:wiz550webds_kr:j1b1211ccd.pdf)', 'tags': 'RJ45 Magjack', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_Cetus_J1B1211CCD.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_RJ : RJ45_Cetus_J1B1211CCD_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

