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


#0: SSH (1) BitTorrent
#1: totalSourceBytes (2) 148502
#2: totalDestinationBytes (2) 3111115
#3: totalDestinationPackets (2) 2755
#4: totalSourcePackets (2) 2219
#5: sourcePayloadAsBase64 (1) E0JpdFRvcnJlbnQgcHJvdG9jb2wAAAAAABAABT4WFX8IeetD6eUfRdSF/v
#6: destinationPayloadAsBase64 (1) E0JpdFRvcnJlbnQgcHJvdG9jb2wAAAAAABAABT4WFX8IeetD6eUfRdSF/v
#7: destinationPayloadAsUTF (1) .BitTorrent protocol..>...y.C...E......r.-TR1930-
#8: direction (1) L2R
#9: sourceTCPFlagsDescription (1) S,P,A
#10: destinationTCPFlagsDescription (1) S,P,A
#11: source (1) 192.168.2.107
#12: protocolName (1) tcp_ip
#13: sourcePort (1) 2328
#14: destination (1) 178.34.121.182
#15: destinationPort (1) 51413
#16: startDateTime (3) (2010, 6, 14, 23, 28, 48)
#17: stopDateTime (3) (2010, 6, 14, 23, 58, 59)
#18: Tag (1) Normal

# text fields with terminate number of values
#0 app name
#8: direction
#12: protocolName

# integer fields
#1: totalSourceBytes
#2: totalDestinationBytes
#3: totalDestinationPackets
#4: totalSourcePackets
#13: sourcePort (1) 2328
#15: destinationPort (1) 51413

# 5, 6, 7 --- payload Base64
# 9 - 10 flags S, P, A

# 11, 14 - source / destination -- temporary omit


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

# file_name = '/home/devil/Downloads/ICX_2012/test.xlsx'
file_name = 'test.xlsx'

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

import base64

enc_string = worksheet.cell_value(1, 6)
# print "Encoded string :", enc_string
print "Decoded base64 :"
print ascii(base64.b64decode(enc_string))

# tag_dict = {}
# while curr_row < num_rows:
# 	curr_row += 1
# 	curr_tag = str(worksheet.cell_value(curr_row, TAG_COLUMN))
# 	if tag_dict.get(curr_tag, None):
# 		tag_dict[curr_tag] += 1
# 	else:
# 		tag_dict[curr_tag] = 1

# print tag_dict
