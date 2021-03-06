import os
from os.path import join, dirname, exists
import numpy as np

publications_dir = join(dirname(os.getcwd()),'_publications')
publication_list = os.listdir(publications_dir)
publication_list = filter(lambda x: '.md' in x, publication_list)
output_file = join(dirname(os.getcwd()),'_pages', 'publications.md')

header = '---\n'
header += 'title: \"Publications\"\n'
header += 'layout: archive\n'
header += 'permalink: /publications/\n'
header += 'author_profile: true\n'
header += '---\n'

journal_to_write = ''
conferences_to_write = ''
workshops_to_write = ''
bookchapters_to_write = ''
abstracts_to_write = ''

dict_to_write = {
	'journals': {},
	'conferences': {},
	'workshops': {},
	'bookchapters': {},
	'abstracts': {}
}

for publication in publication_list:
	print(join(publications_dir,publication))
	with open(join(publications_dir,publication), 'r') as f:
		title = ''
		authors = ''
		venue = ''
		date = ''
		count = 0
		for row in f.readlines():
			if '---' in row:
				count += 1
				if count == 2:
					break

			if 'title' in row:
				title = '<b>[' + row.split('title: ')[1].split('\n')[0] + '](https://acasamitjana.github.io/publications/' + publication.split('.')[0] + ')'
				title += '</b>\n'
			elif 'type' in row:
				publication_type = row.split('type: ')[1].split('\n')[0]
			elif 'venue' in row:
				venue = '<i>' + row.split('venue: ')[1].split('\n')[0] + '</i>'
				venue += ', '
			elif 'authors' in row:
				authors = row.split('authors: ')[1].split('\n')[0]
				authors += '\n'
			elif 'date' in row:
				date = row.split('date: ')[1].split('-')[0] + '.'
				date += '\n'
				complete_date = int(''.join(row.split('date: ')[1].split('-')))


	if publication_type == 'journal':
		for it in range(1000):
			if complete_date + it not in list(dict_to_write['journals'].keys()):
				complete_date = complete_date + it
				break
		dict_to_write['journals'][complete_date] = title + authors + venue + date + '\n\n'
	elif publication_type == 'conference':
		for it in range(1000):
			if complete_date + it not in list(dict_to_write['conferences'].keys()):
				complete_date = complete_date + it
				break
		dict_to_write['conferences'][complete_date] = title + authors + venue + date + '\n\n'
	elif publication_type == 'workshop':
		for it in range(1000):
			if complete_date + it not in list(dict_to_write['workshops'].keys()):
				complete_date = complete_date + it
				break
		dict_to_write['workshops'][complete_date] = title + authors + venue + date + '\n\n'
	elif publication_type == 'bookchapter':
		for it in range(1000):
			if complete_date + it not in list(dict_to_write['bookchapters'].keys()):
				complete_date = complete_date + it
				break
		dict_to_write['bookchapters'][complete_date] = title + authors + venue + date + '\n\n'
	elif publication_type == 'abstract':
		for it in range(1000):
			if complete_date + it not in list(dict_to_write['abstracts'].keys()):
				complete_date = complete_date + it
				break
		dict_to_write['abstracts'][complete_date] = title + authors + venue + date + '\n\n'
	else:
		raise ValueError('Specify a valid #type# of publication')


with open(output_file, 'w') as f:
	f.write(header)
	f.write('\n')
	f.write('\n\n## Journal papers\n\n')
	dates_ordered = np.sort(list(dict_to_write['journals'].keys()))[::-1]
	for date in dates_ordered:
		f.write(dict_to_write['journals'][date])
	
	f.write('\n\n## Conference papers\n\n')
	dates_ordered = np.sort(list(dict_to_write['conferences'].keys()))[::-1]
	for date in dates_ordered:
		f.write(dict_to_write['conferences'][date])
	
	f.write('\n\n## Workshop papers\n\n')
	dates_ordered = np.sort(list(dict_to_write['workshops'].keys()))[::-1]
	for date in dates_ordered:
		f.write(dict_to_write['workshops'][date])
	
	if abstracts_to_write != '':
		f.write('\n\n## Abstracts \n\n')
		dates_ordered = np.sort(list(dict_to_write['abstracts'].keys()))[::-1]
		for date in dates_ordered:
			f.write(dict_to_write['abstracts'][date])
	
	if bookchapters_to_write != '':
		f.write('\n\n## Books chapters\n\n')
		dates_ordered = np.sort(list(dict_to_write['bookchapters'].keys()))[::-1]
		for date in dates_ordered:
			f.write(dict_to_write['bookchapters'][date])



