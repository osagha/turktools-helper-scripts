import csv

conditions = ['context-low-bias', 'context-positive-bias', 'context-negative-bias']
prompt_parts = ['prompt-setup-prior', 'prompt-likelihood']

out_file_lines = []

with open('relevance-items.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    item_counter = 1
    for row in reader:
        for condition in conditions:
            out_file_lines.append('# target ' + str(item_counter) + ' ' + condition)
            out_file_lines.append(row[condition])
            out_file_lines.append('')
            for part in prompt_parts:
                out_file_lines.append(row[part])
            out_file_lines.append('')
            item_counter += 1
print(item_counter)
print(out_file_lines)

with open('relevance-items.txt', 'w') as outfile:
    for line in out_file_lines:
        outfile.write('%s\n' % line)