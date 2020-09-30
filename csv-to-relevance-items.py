import csv

conditions_answer = ['answer-high-certainty', 'answer-low-certainty', 'answer-reductive-answer', 'answer-exhaustive-answer', 'answer-non-answer']
conditions_context = ['context-low-bias', 'context-positive-bias', 'context-negative-bias']


out_file_lines = []

with open('relevance-items-complete.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    item_counter = 1
    for row in reader:
        for answer in conditions_answer:
            for context in conditions_context:
                out_file_lines.append('# target ' + str(item_counter) + ' ' + answer + '-' + context)
                out_file_lines.append(row[context])
                out_file_lines.append(row['setup-relevance-your-turn'])
                out_file_lines.append(row['Question'])
                out_file_lines.append(row['name'] + ' responds:')
                out_file_lines.append(row[answer])
                out_file_lines.append('How helpful was ' + row['name'] + '\'s' + ' response?')
                out_file_lines.append('')
        item_counter += 1
print(item_counter)
print(out_file_lines)

with open('relevance-items.txt', 'w') as outfile:
    for line in out_file_lines:
        outfile.write('%s\n' % line)