s = "CidatyUcityda"
answer = "Udacity"

print answer == s[6] + s[-2:] + s[7:12]
print answer == s[6] + s[-2:] + s[7:11]
print answer == s[6] + s[2:4] + s[7:13]
print answer == s[-7] + s[2:4] + s[7:11]
print answer == s[6] + s[-2] + s[3] + s[-2] + s[4:6]
print answer == s[6] + s[2] + s[3] + s[7:11]
