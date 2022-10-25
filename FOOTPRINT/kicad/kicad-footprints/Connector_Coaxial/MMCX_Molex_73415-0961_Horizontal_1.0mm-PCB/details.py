
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Coaxial"
    oIndex = "MMCX_Molex_73415-0961_Horizontal_1.0mm-PCB"
    hexID = "FZKCNCOACXMX73415961HORIZONTAL1PCB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MMCX_Molex_73415-0961_Horizontal_1.0mm-PCB', 'description': 'Molex MMCX Horizontal Coaxial https://www.molex.com/pdm_docs/sd/734150961_sd.pdf', 'tags': 'Molex MMCX Horizontal Coaxial', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Coaxial.3dshapes/MMCX_Molex_73415-0961_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Coaxial : MMCX_Molex_73415-0961_Horizontal_1.0mm-PCB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

