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


s = letters()
w = "read"
f = s.check_lines(w)
print(f)
d = s.check_words(w)
print(d)






