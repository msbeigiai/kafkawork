
class SqlCommand:
	def __init__(self, name):
		self.key_name = name
		self.commands = ''
		self.enriched_table_name = []

	def return_command(self):
		if 'STORE' in self.key_name:
			temp_string = self.key_name.replace('STORE:', '')
			self.commands = "select c.NAME " \
						"from RETAILCHANNELTABLE a inner join OMOPERATINGUNITVIEW b " \
						"on a.OMOPERATINGUNITID = b.RECID inner join DIRPARTYTABLE c " \
						"ON c.PARTYNUMBER = b.PARTYNUMBER where a.STORENUMBER = '%s'" % temp_string

		elif 'CUSTACCOUNT' in self.key_name:
			temp_string = self.key_name.replace('CUSTACCOUNT:', '')
			self.commands = "select d.name \
							from CUSTTABLE c \
							inner join DIRPARTYTABLE d on c.PARTY = d.RECID \
							where \
							c.ACCOUNTNUM = '%s'" % temp_string

	# def command_custom(self):
	# 	self.commands = "select d.name \
	# 			from CUSTTABLE c \
	# 			inner join DIRPARTYTABLE d on c.PARTY = d.RECID \
	# 			where \
	# 			c.ACCOUNTNUM = " + str(self.name)

# store_num = '1051'
# account_num = 'OSH-018214'
# commnands = {
#     'get_store_name': "select c.NAME from \
# 	RETAILCHANNELTABLE a \
# 	inner join OMOPERATINGUNITVIEW b on a.OMOPERATINGUNITID = b.RECID \
# 	inner join DIRPARTYTABLE c ON c.PARTYNUMBER = b.PARTYNUMBER \
#     where \
# 	a.STORENUMBER = '1051'" ,
# 	'get_costum_name': "select d.name \
# 	from CUSTTABLE c \
# 	inner join DIRPARTYTABLE d on c.PARTY = d.RECID \
# 	where \
# 	c.ACCOUNTNUM = 'OSH-018214'"
# }

# select c.NAME
# from
# 	RETAILCHANNELTABLE a
# 	inner join OMOPERATINGUNITVIEW b on a.OMOPERATINGUNITID = b.RECID
# 	inner join DIRPARTYTABLE c ON c.PARTYNUMBER = b.PARTYNUMBER
# where
# 	a.STORENUMBER = '1051' --store
#
#
# select d.name
# from
# 	CUSTTABLE c
# 	inner join DIRPARTYTABLE d on c.PARTY = d.RECID
# where
# 	c.ACCOUNTNUM = 'OSH-018214'   --custaccount