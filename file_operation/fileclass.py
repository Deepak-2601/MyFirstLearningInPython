class letters:

    def check_lines(self, f1):
        a = open(f1, "r")
        o = len(a.readlines())
        a.close()
        return o

    def check_words(self, f1):
        q = open(f1, "r")
        z = q.read()
        l1 = z.split()
        calculate = len(l1)
        return calculate



if __name__ == "__main__":
    s = letters()
    g = "D:\Deepak\Project\python\service\check_78"
    d = s.check_lines(g)
    print(d)
    e = s.check_words(g)
    print(e)
