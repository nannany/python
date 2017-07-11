class LexmaxReplace:
    def get(self, s, t):
        list_t = list(t)
        list_t.sort(reverse=True)
        print(list_t)


if __name__ == '__main__':

    LexmaxReplace.get("abb", "cd")
