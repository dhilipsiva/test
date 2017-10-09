class Klass(object):

    def just_meth(self):
        print("just_meth", self)

    @classmethod
    def klas_meth(kls):
        print("klas_meth", kls)

    @staticmethod
    def stat_meth():
        print("stat_meth")
