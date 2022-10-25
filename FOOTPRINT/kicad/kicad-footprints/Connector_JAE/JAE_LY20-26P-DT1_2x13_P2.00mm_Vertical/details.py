
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JAE"
    oIndex = "JAE_LY20-26P-DT1_2x13_P2.00mm_Vertical"
    hexID = "FZKCNJAEJAELY226PDT12X13P2VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JAE_LY20-26P-DT1_2x13_P2.00mm_Vertical', 'description': 'Molex LY 20 series connector, LY20-26P-DT1, 13 Circuits (http://www.jae.com/z-en/pdf_download_exec.cfm?param=SJ103130.pdf), generated with kicad-footprint-generator', 'tags': 'connector JAE  side entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JAE.3dshapes/JAE_LY20-26P-DT1_2x13_P2.00mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_JAE : JAE_LY20-26P-DT1_2x13_P2.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

