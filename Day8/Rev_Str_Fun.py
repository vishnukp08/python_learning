def string_reverse(s):

    if s == "":
        return s
    
    return string_reverse(s[1:]) + s[0] 
print(string_reverse("hello world"))