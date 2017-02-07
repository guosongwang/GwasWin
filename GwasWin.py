#!/usr/bin/python

import sys
from optparse import OptionParser


class GwasWin:
	def __init__(self, options):
		self.input = open(sys.argv[-1], 'r')
		self.output = open(options.output + 'GWAS.slided.txt', 'w')

	def gwas_sliding_window(self, options):

		window = int(options.size)

		length = {'Chr1': 158337067, 'Chr2': 137060424, 'Chr3': 121430405, 'Chr4': 120829699, 'Chr5': 121191424,
		          'Chr6': 119458736, 'Chr7': 112638659, 'Chr8': 113384836, 'Chr9': 105708250, 'Chr10': 104305016,
		          'Chr11': 107310763, 'Chr12': 91163125, 'Chr13': 84240350, 'Chr14': 84648390, 'Chr15': 85296676,
		          'Chr16': 81724687, 'Chr17': 75158596, 'Chr18': 66004023, 'Chr19': 64057457, 'Chr20': 72042655,
		          'Chr21': 71599096, 'Chr22': 61435874, 'Chr23': 52530062, 'Chr24': 62714930, 'Chr25': 42904170,
		          'Chr26': 51681464, 'Chr27': 45407902, 'Chr28': 46312546, 'Chr29': 51505224, 'Chr30': 148823899}

		chromosomes = {}

		for key in length.keys():
			bin_total = (length[key] / window) + 2
			chromosomes[key] = {}
			for i in range(1, bin_total):
				bin_tag = 'bin' + str(i)
				chromosomes[key][bin_tag] = {}
				chromosomes[key][bin_tag]['beta_list'] = []

		print 'Constructing windows for each chromosome complete. '

		for line in self.input:
			if not line.startswith('CHR') and not line.startswith('0'):
				line = line.rstrip()
				parts = line.split('\t')
				chromosome = 'Chr' + str(parts[0])
				position = int(parts[2])
				beta = float(parts[7])
				bin_tag = 'bin' + str((position / window) + 1)
				chromosomes[chromosome][bin_tag]['beta_list'].append(beta)

		print 'Collecting information for each window complete. '

		print>>self.output, 'Chr' + '\t' + 'start' + '\t' + 'end' + '\t' + 'value'

		for chrom in chromosomes:
			for win in chromosomes[chrom]:
				chromosomes[chrom][win]['beta_avg'] = sum(chromosomes[chrom][win]['beta_list']) / (
					len(chromosomes[chrom][win]['beta_list']) + 1)
				chromosomes[chrom][win]['start'] = int(win.lstrip('bin')) * window
				chromosomes[chrom][win]['end'] = ((int(win.lstrip('bin')) + 1) * window) - 1
				if chromosomes[chrom][win]['end'] >= length[chrom]:
					chromosomes[chrom][win]['end'] = length[chrom]
				else:
					pass

				print>>self.output, str(chrom) + '\t' + str(chromosomes[chrom][win]['start']) + '\t' + str(
					chromosomes[chrom][win]['end']) + '\t' + str(chromosomes[chrom][win]['beta_avg'])

		print 'Calculation done. Job was finished! '

		self.input.close()
		self.output.close()


def main():
	usage = 'Usage: python GwasWin.py [Options] file'
	parser = OptionParser(usage=usage)
	parser.add_option('-o', '--output_path', action='store', type='string', dest='output', help='Define output path.')
	parser.add_option('-s', '--size_window', action='store', type='int', dest='size', help='Define window size.')
	(options, args) = parser.parse_args()
	GwasWin(options).gwas_sliding_window(options)


if __name__ == '__main__':

	try:
		main()
	except KeyboardInterrupt:
		sys.stderr.write("User interrupts me! See you!\n")
		sys.exit(0)
