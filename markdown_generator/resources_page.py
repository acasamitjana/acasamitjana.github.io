import os
from os.path import join, dirname, exists, isdir

resources_dir = join(dirname(os.getcwd()),'_resources')
resources_list = os.listdir(resources_dir)
resources_list = filter(lambda x: '.md' in x, resources_list)
output_file = join(dirname(os.getcwd()),'_pages', 'resources.md')

header = '---\n'
header += 'title: \"Resources\"\n'
header += 'layout: archive\n'
header += 'permalink: /resources/\n'
header += 'author_profile: true\n'
header += '---\n'

dict_to_write = {
	'software': {},
	'presentations': {}
}

for resource in resources_list:
	dict_tmp = {'title': '', 'resourceurl': '', 'code':'', 'authors':'', 'shortdescription': ''}
	with open(join(resources_dir, resource), 'r') as f:
		count = 0
		for row in f.readlines():
			if '---' in row:
				count += 1
				if count == 2:
					break

			if 'title' in row:
				dict_tmp['title'] += '<b>[' + row.split('title: ')[1].split('\n')[0] + '](https://acasamitjana.github.io/personal-webpage-jekyll/resources/' + resource.split('.')[0] + ')'
			elif 'type' in row:
				resource_type = row.split('type: ')[1].split('\n')[0]
			elif 'resourceurl' in row:
				dict_tmp['resourceurl'] += row.split('resourceurl: ')[1].split('\n')[0]
			elif 'authors' in row:
				dict_tmp['authors'] += row.split('authors: ')[1].split('\n')[0]
			elif 'code' in row:
				dict_tmp['code'] += row.split('code: ')[1].split('\n')[0]
			elif 'shortdescription' in row:
				dict_tmp['shortdescription'] += row.split('shortdescription: ')[1].split('\n')[0]
	dict_to_write[resource_type][resource] = dict_tmp 

with open(output_file, 'w') as f:
	f.write(header)
	f.write('\n')
	f.write('\n\n## Software\n\n')
	for key_r, dict_r in dict_to_write['software'].items():
		to_write = dict_r['title'] + '<br/>' + '\n' + 'Authors: ' + dict_r['authors'] + '<br/>' + '\n'
		to_write += '<p>' + dict_r['shortdescription'] + '</p>\n'
		if 'resourceurl' in list(dict_r.keys()):
			to_write += '[[Resource URL](' + dict_r['resourceurl'] + ')]' + '\n'
		if 'code' in list(dict_r.keys()):
			to_write += '[[Code](' + dict_r['code'] + ')]' + '\n'
		f.write(to_write)
	
	for key_r, dict_r in dict_to_write['presentations'].items():
		to_write = dict_r['title'] + '<br/>' + '\n' + 'Authors:' + dict_r['authors'] + '<br/>' + '\n'
		to_write += '<p>' + dict_r['shortdescription'] + '</p>\n'
		if 'resourceurl' in list(dict_r.keys()):
			to_write += '[[Resource URL](' + dict_r['resourceurl'] + ')]' + '\n'
		if 'code' in list(dict_r.keys()):
			to_write += '[[Code](' + dict_r['code'] + ')]' + '\n'
		f.write(to_write)
	


