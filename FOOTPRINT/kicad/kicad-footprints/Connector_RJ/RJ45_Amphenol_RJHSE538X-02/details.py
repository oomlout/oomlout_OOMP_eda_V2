
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_RJ"
    oIndex = "RJ45_Amphenol_RJHSE538X-02"
    hexID = "FZKCNRJRJ45AMPHENOLRJHSE538X2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RJ45_Amphenol_RJHSE538X-02', 'description': 'Shielded, 2 LED, 2 Ports, http://www.amphenolinfocom.eu/NavData/Drawings/RJHSE-538X-02-REVC.pdf', 'tags': 'RJ45 8p8c dual ethernet cat5', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_Amphenol_RJHSE538X-02.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_RJ : RJ45_Amphenol_RJHSE538X-02')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

