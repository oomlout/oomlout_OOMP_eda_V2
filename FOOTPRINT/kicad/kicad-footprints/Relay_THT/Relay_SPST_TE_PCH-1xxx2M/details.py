
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_SPST_TE_PCH-1xxx2M"
    hexID = "FZKRELRELAYSPSTTEPCH1XXX2M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_SPST_TE_PCH-1xxx2M', 'description': 'Miniature PCB Relay, PCH Series, 1 Form A (NO), SPST http://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Data+Sheet%7FPCH_series_relay_data_sheet_E%7F1215%7Fpdf%7FEnglish%7FENG_DS_PCH_series_relay_data_sheet_E_1215.pdf', 'tags': 'Relay SPST NO', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_SPST_TE_PCH-1xxx2M.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Relay_THT : Relay_SPST_TE_PCH-1xxx2M')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

