import xlrd

files = [
"TestbedMonJun14.xlsx",
"TestbedSatJun12.xlsx",
"TestbedSunJun13.xlsx",
"TestbedThuJun17a.xlsx",
"TestbedThuJun17b.xlsx",
"TestbedThuJun17c.xlsx",
"TestbedTueJun15a.xlsx",
"TestbedTueJun15b.xlsx",
"TestbedTueJun15c.xlsx",
"TestbedWedJun16a.xlsx",
"TestbedWedJun16b.xlsx",
"TestbedWedJun16c.xlsx"]


#0: appName
#1: totalSourceBytes
#2: totalDestinationBytes
#3: totalDestinationPackets
#4: totalSourcePackets
#5: sourcePayloadAsBase64
#6: destinationPayloadAsBase64
#7: destinationPayloadAsUTF
#8: direction
#9: sourceTCPFlagsDescription
#10: destinationTCPFlagsDescription
#11: source
#12: protocolName
#13: sourcePort
#14: destination
#15: destinationPort
#16: startDateTime
#17: stopDateTime
#18: Tag

def get_cell_value(cell_value, cell_type):
	if cell_type == xlrd.XL_CELL_EMPTY:
		return None
	elif cell_type == xlrd.XL_CELL_TEXT:
		return cell_value
	elif cell_type == xlrd.XL_CELL_NUMBER:
		return int(cell_value)
	elif cell_type == xlrd.XL_CELL_DATE:
		return xlrd.xldate_as_tuple(cell_value, workbook.datemode)
	elif cell_type == xlrd.XL_CELL_BOOLEAN:
		return bool(cell_value)
	else:
		return cell_value

print 'CELL_TEXT', xlrd.XL_CELL_TEXT

file_name = '/home/devil/Downloads/ICX_2012/test.xlsx'

workbook = xlrd.open_workbook(file_name)
worksheet = workbook.sheet_by_index(0)

num_rows = worksheet.nrows - 1
print "Rows number :", num_rows

curr_row = 0
TAG_COLUMN = 19

for cell_num in xrange(0, TAG_COLUMN):
	cell_value = worksheet.cell_value(curr_row, cell_num)
	cell_type = worksheet.cell_type(curr_row + 1, cell_num)
	print "#%d: %s (%s)" % (cell_num, cell_value, cell_type), get_cell_value(worksheet.cell_value(curr_row + 1, cell_num), worksheet.cell_type(curr_row + 1, cell_num))
# tag_dict = {}
# while curr_row < num_rows:
# 	curr_row += 1
# 	curr_tag = str(worksheet.cell_value(curr_row, TAG_COLUMN))
# 	if tag_dict.get(curr_tag, None):
# 		tag_dict[curr_tag] += 1
# 	else:
# 		tag_dict[curr_tag] = 1

# print tag_dict