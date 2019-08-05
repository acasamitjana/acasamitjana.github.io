import os
from os.path import join, dirname, exists

publications_dir = join(dirname(os.getcwd()),'_publications')
publication_list = os.listdir(publications_dir)
publication_list = filter(lambda x: '.md' in x, publication_list)
output_file = join(dirname(os.getcwd()),'_pages', 'publications.md')

header = '---\n'
header += 'title: \" Publications\"\n'
header += 'layout: archive\n'
header += 'permalink: publications/\n'
header += 'author_profile: true\n'
header += '---\n'

journal_to_write = ''
conferences_to_write = ''
workshops_to_write = ''
bookchapters_to_write = ''
abstracts_to_write = ''

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
				title = '<b>[' + row.split('title: ')[1].split('\n')[0] + '](https://acasamitjana.github.io/personal-webpage-jekyll/' + publication.split('.')[0] + ')'
				title += '</b>\n'
			elif 'type' in row:
				publication_type = row.split('type: ')[1].split('\n')[0]
			elif 'venue' in row:
				venue = '<i>' + row.split('venue: ')[1].split('\n')[0] + '</i>'
				venue += '\n'
			elif 'authors' in row:
				authors = row.split('authors: ')[1].split('\n')[0]
				authors += ', '
			elif 'date' in row:
				print(row)
				date = row.split('date: ')[1].split('-')[0] + '.'
				date += '\n'


	if publication_type == 'journal':
		journal_to_write += title + authors + venue + date
		journal_to_write += '\n\n'
	elif publication_type == 'conference':
		conferences_to_write += title + authors + venue + date
		conferences_to_write += '\n\n'
	elif publication_type == 'workshop':
		workshops_to_write += title + authors + venue + date
		workshops_to_write += '\n\n'
	elif publication_type == 'bookchapter':
		bookchapters_to_write += title + authors + venue + date
		journal_to_write += '\n\n'
	elif publication_type == 'abstract':
		abstracts_to_write += title + authors + venue + date
		abstracts_to_write += '\n\n'
	else:
		raise ValueError('Specify a valid #type# of publication')


with open(output_file, 'w') as f:
	f.write(header)
	f.write('\n')
	f.write('\n\n## Journal papers\n\n')
	f.write(journal_to_write)
	f.write('\n\n## Conference papers\n\n')
	f.write(conferences_to_write)
	f.write('\n\n## Workshop papers\n\n')
	f.write(workshops_to_write)
	if abstracts_to_write != '':
		f.write('\n\n## Abstracts \n\n')
		f.write(abstracts_to_write)
	if bookchapters_to_write != '':
		f.write('\n\n## Books chapters\n\n')
		f.write(bookchapters_to_write)



