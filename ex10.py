class BackSlash(object):

    def __init__(self, tabby_cat, persian_cat, backslash_cat, fat_cat):
        self.tabby_cat = tabby_cat
        self.persian_cat = persian_cat
        self.backslash_cat = backslash_cat
        self.fat_cat = fat_cat

    def print_it(self):
        return "{} {} {} {}".format(self.tabby_cat, self.persian_cat, self.backslash_cat, self.fat_cat)

