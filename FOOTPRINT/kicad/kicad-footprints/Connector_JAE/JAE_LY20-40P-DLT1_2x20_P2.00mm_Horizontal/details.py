
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JAE"
    oIndex = "JAE_LY20-40P-DLT1_2x20_P2.00mm_Horizontal"
    hexID = "FZKCNJAEJAELY24PDLT12X2P2HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JAE_LY20-40P-DLT1_2x20_P2.00mm_Horizontal', 'description': 'Molex LY 20 series connector, LY20-40P-DLT1, 20 Circuits (http://www.jae.com/z-en/pdf_download_exec.cfm?param=SJ038187.pdf), generated with kicad-footprint-generator', 'tags': 'connector JAE  top entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JAE.3dshapes/JAE_LY20-40P-DLT1_2x20_P2.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JAE : JAE_LY20-40P-DLT1_2x20_P2.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

