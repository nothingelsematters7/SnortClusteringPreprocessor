import csv

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


values_list = {}

def convert_symbol_field(num, value):
    if num not in values_list:
        d = {value: 0}
        values_list[num] = d
        return 0
    else:
        d = values_list[num]
        if value in d:
            return d[value]
        else:
            result = len(d)
            d[value] = result
            return result


FLAGS = {'S': 1, 'P': 2, 'A': 4, 'F': 8, 'R': 16}

def convert_flags_field(value):
    '''
    Convert a field like S,P,A -> integer
    '''
    if not value or value == 'N/A':
        return 0
    else:
        flags = value.split(',')
        result = 0
        for flag in flags:
            result += FLAGS.get(flag, 0)
        return result


VALUABLE_COLUMNS = [0, 1, 2, 3, 4, 8, 9, 10, 12, 13, 15, 18]

with open('/home/devil/Dropbox/studying/TestbedMonJun14.csv', 'rUb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    with open('output.csv', 'wb') as csvout:
        spamwriter = csv.writer(csvout, delimiter=';')
        for read_row in spamreader:
            if spamreader.line_num == 1:
                spamwriter.writerow([read_row[i] for i in VALUABLE_COLUMNS])
                continue
            try:
                row = []
                row.append(convert_symbol_field(0, read_row[0]))
                row.append(read_row[1])
                row.append(read_row[2])
                row.append(read_row[3])
                row.append(read_row[4])
                row.append(convert_symbol_field(8, read_row[8]))
                row.append(convert_flags_field(read_row[9]))
                row.append(convert_flags_field(read_row[10]))
                row.append(convert_symbol_field(12, read_row[12]))
                row.append(read_row[13])
                row.append(read_row[15])
                row.append(convert_symbol_field(18, read_row[18]))

                spamwriter.writerow(row)

            except Exception, e:
                print "#", spamreader.line_num
                print read_row

                raise e
