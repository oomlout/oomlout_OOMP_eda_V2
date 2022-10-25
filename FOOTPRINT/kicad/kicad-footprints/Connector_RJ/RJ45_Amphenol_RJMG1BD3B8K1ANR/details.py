
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_RJ"
    oIndex = "RJ45_Amphenol_RJMG1BD3B8K1ANR"
    hexID = "FZKCNRJRJ45AMPHENOLRJMG1BD3B8K1ANR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RJ45_Amphenol_RJMG1BD3B8K1ANR', 'description': '1 Port RJ45 Magjack Connector Through Hole 10/100 Base-T, AutoMDIX, https://www.amphenolcanada.com/ProductSearch/Drawings/AC/RJMG1BD3B8K1ANR.PDF', 'tags': 'RJ45 Magjack', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_Amphenol_RJMG1BD3B8K1ANR.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_RJ : RJ45_Amphenol_RJMG1BD3B8K1ANR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

