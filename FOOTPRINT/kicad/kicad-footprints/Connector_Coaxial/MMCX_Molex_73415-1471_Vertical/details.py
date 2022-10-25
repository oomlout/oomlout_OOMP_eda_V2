
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Coaxial"
    oIndex = "MMCX_Molex_73415-1471_Vertical"
    hexID = "FZKCNCOACXMX734151471VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MMCX_Molex_73415-1471_Vertical', 'description': 'http://www.molex.com/pdm_docs/sd/734151471_sd.pdf', 'tags': 'Molex MMCX Coaxial Connector 50 ohms Female Jack Vertical THT', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Coaxial.3dshapes/MMCX_Molex_73415-1471_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Coaxial : MMCX_Molex_73415-1471_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

